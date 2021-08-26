import graphene
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
        
class ConnectionsQuery(graphene.ObjectType):
    requests = graphene.List(ConnectionRequestType)
    
    def resolve_requests(root, info, **kwargs):
        """Returns all user's requests pending of approval. 
        """
        user = info.context.user
        if not user.is_anonymous:
            return ConnectionRequest.objects.filter(accepted=False, to_user=user.id).order_by('-request_date')
        else:
            raise Exception('Not logged in!')