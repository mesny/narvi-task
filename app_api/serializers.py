from rest_framework import serializers
from tutorial.quickstart.serializers import GroupSerializer

from .models import Group, Token



class TokenSerializer(serializers.ModelSerializer):
    # group = GroupSerializer(many=False, read_only=False)
    class Meta:
        model = Token
        fields = ['group_id', 'id', 'value', 'created', 'updated']
        read_only_fields = ['id', 'created', 'updated']



class GroupSerializer(serializers.ModelSerializer):
    tokens = TokenSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['id', 'name', 'version', 'created', 'updated', 'tokens']
        read_only_fields = ['id', 'version', 'created', 'updated', 'tokens']


