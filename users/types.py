import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserNode
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

class UserQuery(graphene.ObjectType):
    all_users = graphene.List(UserNode, username=graphene.String())
    user = graphene.Field(UserNode, pk=graphene.Int())

    
    def resolve_user(_, info, pk):
        """Search the user with the ID equal to the PK passed as parameter
        """
        user = info.context.user
        if not user.is_anonymous:
            if pk != user.id:
                res= User.objects.filter(pk=pk)
                return res.first()
            else:
                raise Exception('Are you trying to looking for yourself?')
        else:
            raise Exception('Not logged in!')
        
    def resolve_all_users(_, info, username=None):
        """Search and return for other users. 

        Args:
            username (str, optional): username to filter the users. Defaults to None.
        """
        user = info.context.user
        if not user.is_anonymous:
            
            if username:
                res= User.objects.filter(username__icontains=username).exclude(pk=user.id)
            else:
                res = User.objects.all().exclude(pk=user.id)
                
            return res
        else:
            raise Exception('Not logged in!')
        
class ConnectionQuery(graphene.ObjectType):
    requests = graphene.List(ConnectionRequestType)
    followers = graphene.List(ConnectionRequestType)
    follows = graphene.List(ConnectionRequestType)
    
    def resolve_requests(root, info, **kwargs):
        """Returns all user's requests pending of approval. 
        """
        user = info.context.user
        if not user.is_anonymous:
            return ConnectionRequest.objects.filter(accepted=False, to_user=user.id).order_by('-request_date')
        else:
            raise Exception('Not logged in!')
        
    def resolve_followers(root, info, **kwargs):
        """Returns all user's followers. 
        """
        user = info.context.user
        if not user.is_anonymous:
            return ConnectionRequest.objects.filter(accepted=True, to_user=user.id).order_by('-request_date')
        else:
            raise Exception('Not logged in!')
    
    def resolve_follows(root, info, **kwargs):
        """Returns all user's follows. 
        """
        user = info.context.user
        if not user.is_anonymous:
            return ConnectionRequest.objects.filter(accepted=True, from_user=user.id).order_by('-request_date')
        else:
            raise Exception('Not logged in!')
