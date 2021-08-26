import graphene
from django.db.models import Q
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
    user_ideas = graphene.List(IdeaType)
    
    def resolve_ideas(root, info, **kwargs):
        """Returns all the public ideas + user ideas (if logged). 
        """
        user = info.context.user
        all_ideas = Idea.objects.all()
        
        # Always get the Public ideas
        res_ideas = all_ideas.filter(visibility=Idea.Visibility.public)
        # And if the user is logged, merge with the user (non public) ideas to return them all
        if not user.is_anonymous:    
            res_ideas = res_ideas | all_ideas.filter(user_id=user.id)
            
        return res_ideas.order_by('-created_at')

    def resolve_user_ideas(root, info, **kwargs):
        """Get only the logged user ideas
        """
        user = info.context.user
        if not user.is_anonymous:
            return Idea.objects.all().filter(user_id=user.id)
        else:
            raise Exception('Not logged in!')