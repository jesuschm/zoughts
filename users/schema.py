import graphene
from graphql_auth import mutations
from .models import User, ConnectionRequest
from .types import UserType, ConnectionRequestType, ConnectionsQuery
from graphql_auth.schema import UserQuery, MeQuery

class CreateConnectionRequestMutation(graphene.Mutation):
    """Create a connection request from the logged user to another, specified through the param user_id
    """
    class Arguments:
        # Mutation to create a connection request
        user_id = graphene.Int()

    # Class attributes define the response of the mutation
    connection_request = graphene.Field(ConnectionRequestType)

    @classmethod
    def mutate(cls, root, info, user_id):
        user = info.context.user
        if not user.is_anonymous:
            if user.id != user_id:   
                connection_request = ConnectionRequest()
                connection_request.to_user = User.objects.get(pk=user_id)
                connection_request.from_user = user
                connection_request.save()
                
                return CreateConnectionRequestMutation(connection_request=connection_request)
            else:
                raise Exception('Sorry. You can\'t connect with yourself. Paradoxically.')
        else:
            raise Exception('Not logged in!')  
        
class AcceptConnectionRequestMutation(graphene.Mutation):
    """Accepts a connection request if you are the destination user.
    """
    class Arguments:
        user_id = graphene.Int()
        
    connection_request = graphene.Field(ConnectionRequestType)
    
    @classmethod
    def mutate(cls, root, info, user_id):
        user = info.context.user
        if not user.is_anonymous:
            connection_request = ConnectionRequest.objects.get(to_user=user.id, from_user=user_id, accepted=False)
            
            connection_request.accepted = True
            connection_request.save()
            
            return AcceptConnectionRequestMutation(connection_request=connection_request)
        else:
            raise Exception('Not logged in!')
        
class DeclineConnectionRequestMutation(graphene.Mutation):
    """Declines a connection request if you are the destination user.
    """
    class Arguments:
        user_id = graphene.Int()
        
    connection_request = graphene.Field(ConnectionRequestType)
    
    @classmethod
    def mutate(cls, root, info, user_id):
        user = info.context.user
        if not user.is_anonymous:
            connection_request = ConnectionRequest.objects.get(to_user=user.id, from_user=user_id, accepted=False)
            connection_request.delete()

            return None
        else:
            raise Exception('Not logged in!')

class DeleteFollowerMutation(graphene.Mutation):
    """Delete a user as a follower.
    """
    class Arguments:
        user_id = graphene.Int()
        
    connection_request = graphene.Field(ConnectionRequestType)
    
    @classmethod
    def mutate(cls, root, info, user_id):
        user = info.context.user
        if not user.is_anonymous:
            connection_request = ConnectionRequest.objects.get(from_user=user_id, to_user=user.id, accepted=True)
            connection_request.delete()

            return None
        else:
            raise Exception('Not logged in!')
        
        
class DeleteFollowMutation(graphene.Mutation):
    """Delete the follow to an user.
    """
    class Arguments:
        user_id = graphene.Int()
        
    connection_request = graphene.Field(ConnectionRequestType)
    
    @classmethod
    def mutate(cls, root, info, user_id):
        user = info.context.user
        if not user.is_anonymous:
            connection_request = ConnectionRequest.objects.get(from_user=user.id, to_user=user_id, accepted=True)
            connection_request.delete()

            return None
        else:
            raise Exception('Not logged in!')
    
class Mutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    refresh_token = mutations.RefreshToken.Field()
    
    create_connection_request = CreateConnectionRequestMutation.Field()
    accept_connection_request = AcceptConnectionRequestMutation.Field()
    decline_connection_request = DeclineConnectionRequestMutation.Field()
    delete_follower = DeleteFollowerMutation.Field()
    delete_follow = DeleteFollowMutation.Field()
    
class Query(UserQuery, MeQuery, ConnectionsQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)