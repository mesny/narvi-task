from functools import reduce
from collections import defaultdict

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction, DatabaseError

from app_api.models import Group as GroupModel, Token as TokenModel



class Group:
    """
    A class dedicated as item class for defaultdict(),
    while parsing the directory structure.
    """
    def __str__(self):
        return f"Group([{reduce(lambda n, n_next: n + " " + n_next, self.nodes, "").lstrip()}])"

    def __repr__(self):
        return str(self)

    def __init__(self):
        self.nodes = []

    def add_node(self, node: str) -> None:
        self.nodes.append(node)



def _get_json(file_name: str, delimiter: str) -> dict:
    """
    Loads the directory structure file and returns JSON
    :param file_name: the file name we want to load directory structure from
    :param delimiter: the delimiter separating name segments
    :return: JSON
    """
    with open(file_name) as fp:
        groups = defaultdict(Group)
        [groups[s[:s.rfind(delimiter)]].add_node(s[s.rfind(delimiter)+1:]) for s
            in filter(lambda l: l != "", [line.strip() for line in fp])]

        json = {}
        for k, v in groups.items():
            json[k] = v.nodes

        return json



def _assert_file_existence(base_file_name: str) -> None:
    file_path = settings.BASE_DIR / base_file_name
    if not file_path.is_file():
        raise FileNotFoundError(file_path)



def _persist(json: dict) -> None:
    with transaction.atomic():
        for group_name, tokens in json.items():
            group = GroupModel(name=group_name)
            group.save()
            for token_str in tokens:
                token = TokenModel(value=token_str, group=group)
                token.save()



class Command(BaseCommand):
    help = 'Add initial JSON structure to database'

    def handle(self, *args, **options):
        """
        Parses the CSV file and saves the directory -> []names structure to database,
        relations app_api_groups and app_api_tokens.
        Accepts base_file_name and delimiter string as arguments.
        """

        base_file_name = options['base_file_name']
        delimiter = options['delimiter']

        _assert_file_existence(base_file_name)
        json = _get_json(base_file_name, delimiter)

        self.stdout.write(self.style.SUCCESS(
            f"Successfully parsed file ({base_file_name})"
        ))

        try:
            _persist(json)
        except DatabaseError as e:
            self.stdout.write(self.style.ERROR(
                f"Error performing database queries: ({e})"
            ))
        else:
            self.stdout.write(self.style.SUCCESS(
                "Successfully saved"
            ))


    def add_arguments(self, parser):
        parser.add_argument('base_file_name', type=str)
        parser.add_argument('delimiter', type=str)

