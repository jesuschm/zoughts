from graphene_django.types import DjangoObjectType
from .models import User, ConnectionRequest

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email')
        
class ConnectionRequestType(DjangoObjectType):
    class Meta:
        model = ConnectionRequest
        fields = (
            'id',
            'from_user', 
            'to_user', 
            'request_date',
            'accepted'
        )