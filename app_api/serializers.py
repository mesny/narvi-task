from rest_framework import serializers
from .models import Group, Token



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['group', 'id', 'value', 'created', 'updated']



class GroupSerializer(serializers.ModelSerializer):
    tokens = TokenSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['id', 'name', 'version', 'created', 'updated', 'tokens']


