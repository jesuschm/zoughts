import graphene
from .types import IdeaType, Query as IdeaQuery
from .models import Idea
from users.models import User
from users.types import UserType

class CreateIdea(graphene.Mutation):
    class Arguments:
        # Mutation to create an idea
        content = graphene.String(required=True)
        visibility = graphene.String(default_value=Idea.Visibility.public.value)
        user_id = graphene.Int()

    # Class attributes define the response of the mutation
    idea = graphene.Field(IdeaType)

    @classmethod
    def mutate(cls, root, info, content, visibility, user_id):
        idea = Idea()
        idea.content = content
        idea.visibility = Idea.Visibility(visibility)
        idea.user = User.objects.get(id=user_id)
        idea.save()
        
        return CreateIdea(idea=idea)
    
class UpdateIdea(graphene.Mutation):
    class Arguments:
        # Mutation to update an idea's visibility.
        visibility = graphene.String(required=True)
        id = graphene.ID()

    idea = graphene.Field(IdeaType)

    @classmethod
    def mutate(cls, root, info, visibility, id):
        idea = Idea.objects.get(pk=id)
        idea.visibility = Idea.Visibility(visibility)
        idea.save()
        
        return UpdateIdea(idea=idea)

class Query(IdeaQuery, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    create_idea = CreateIdea.Field()
    update_idea = UpdateIdea.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)