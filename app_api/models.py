
# CREATE EXTENSION IF NOT EXISTS "pgcrypto";

import uuid
from django.db import models, IntegrityError
from django.core.validators import MinLengthValidator, ValidationError



def validate_min_length_of_1(value):
    stripped = value.strip()
    if len(stripped) < 1:
        raise ValidationError(f"Value must be at least 1 without whitespace, given({stripped})")




class Group(models.Model):
    """
    Model representing a directory name (Group)
    having one or more Tokens
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, editable=True, max_length=200, validators=[validate_min_length_of_1])
    version = models.PositiveIntegerField(default=1, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'created'
        ordering = ['created']

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"model Group({self.name})"



class Token(models.Model):
    """
    Model representing a string value (Token)
    associated with a directory (Group).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tokens')
    value = models.CharField(max_length=255, validators=[validate_min_length_of_1])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['group', 'value'], name='unique_in_group')]
        get_latest_by = 'created'
        ordering = ['created']

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"model Token({self.value}) of Group({self.group.name})"


