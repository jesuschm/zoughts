import graphene
from graphene_django.types import DjangoObjectType
from .models import Idea

class IdeaType(DjangoObjectType):
    class Meta:
        model = Idea
        fields = (
            'id',
            'content',
            'visibility',
            'created_at',
            'user')

class Query(graphene.ObjectType):
    ideas = graphene.List(IdeaType)
    
    def resolve_ideas(root, info, **kwargs):
        return Idea.objects.all()