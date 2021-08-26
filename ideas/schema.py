import graphene
from .types import IdeaType, Query as IdeaQuery
from .models import Idea
from users.models import User
from users.types import UserType

class CreateIdeaMutation(graphene.Mutation):
    class Arguments:
        # Mutation to create an idea
        content = graphene.String(required=True)
        visibility = graphene.String(default_value=Idea.Visibility.public.value)
        user_id = graphene.Int()

    # Class attributes define the response of the mutation
    idea = graphene.Field(IdeaType)

    @classmethod
    def mutate(cls, root, info, content, visibility):
        user = info.context.user
        if not user.is_anonymous:
            idea = Idea()
            idea.content = content
            idea.visibility = Idea.Visibility(visibility)
            idea.user = User.objects.get(id=user.id)
            idea.save()
            
            return CreateIdeaMutation(idea=idea)
        else:
            raise Exception('Not logged in!')
    
class UpdateIdeaMutation(graphene.Mutation):
    class Arguments:
        # Mutation to update an idea's visibility.
        visibility = graphene.String(required=True)
        id = graphene.ID()

    idea = graphene.Field(IdeaType)

    @classmethod
    def mutate(cls, root, info, visibility, id):
        user = info.context.user
        if not user.is_anonymous:
            idea = Idea.objects.get(pk=id, user_id=user.id)
            idea.visibility = Idea.Visibility(visibility)
            idea.save()
            
            return UpdateIdeaMutation(idea=idea)
        else:
            raise Exception('Not logged in!')
        

class Query(IdeaQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    create_idea = CreateIdeaMutation.Field()
    update_idea = UpdateIdeaMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)