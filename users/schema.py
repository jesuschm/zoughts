import graphene
from graphql_auth import mutations
from .models import User, ConnectionRequest
from .types import UserType, ConnectionRequestType
from graphql_auth.schema import UserQuery, MeQuery

class CreateConnectionRequestMutation(graphene.Mutation):
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
                import pdb; pdb.set_trace()
                connection_request.to_user = User.objects.get(pk=user_id)
                connection_request.from_user = user
                connection_request.save()
                
                return CreateConnectionRequestMutation(connection_request=connection_request)
            else:
                raise Exception('Sorry. You can\'t connect with yourself. Paradoxically.')
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
    
class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)