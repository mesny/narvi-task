from django.core.management.base import BaseCommand
from django.db import transaction

from app_api.models import Group, Token



class Command(BaseCommand):
    help = 'Clear directory structure, tables app_api_groups and app_api_tokens'


    def handle(self, *args, **options):
        """
        Clears directory structure, relations app_api_groups and app_api_tokens.
        @todo add some human interaction here, in order to prevent accidental deletions.
        """
        with transaction.atomic():
            Group.objects.all().delete()
            Token.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(
            'Successfully cleared tables app_api_groups and app_api_tokens'
        ))

