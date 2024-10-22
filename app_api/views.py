
from django.shortcuts import get_object_or_404
from django.db import DatabaseError

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import Group, Token
from .serializers import GroupSerializer, TokenSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing group instances.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class TokenViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing token instances.
    """
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    @action(detail=True, methods=['patch'], url_path='move')
    def move(self, request, pk=None):
        """
        A special method for moving a Token from one directory to another.

        """
        token = get_object_or_404(Token, pk=pk)

        new_group_id = request.data.get('target_group_id')
        new_group = get_object_or_404(Group, pk=new_group_id)
        token.group = new_group

        try:
            token.save()
        except DatabaseError as e:
            print (f"Error caught: ({e})")
            status_code = status.HTTP_409_CONFLICT
        else:
            status_code = status.HTTP_200_OK
        finally:
            serializer = TokenSerializer(token, context={ 'request': request })
            return Response(serializer.data, status_code)
