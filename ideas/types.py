import graphene
from django.db.models import Q
from graphene_django.types import DjangoObjectType
from .models import Idea
from users.models import ConnectionRequest

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
    timeline = graphene.List(IdeaType)
    user_ideas = graphene.List(IdeaType, user_id=graphene.Int())
    self_ideas = graphene.List(IdeaType)
    
    def resolve_self_ideas(root, info, **kwargs):
        """Get only the logged user ideas"""
        user = info.context.user
        if not user.is_anonymous:
            return Idea.get_self_ideas(my_user_id= user.id)
        else:
            raise Exception('Not logged in!')
            
    def resolve_user_ideas(root, info, user_id, **kwargs):
        """Get the specific user ideas (public and protected if there is a connection)
        """
        user = info.context.user
        if not user.is_anonymous:
            if user_id == user.id:
                res_ideas = Idea.get_self_ideas(my_user_id= user.id) # Same case that resolve_self_ideas because youre looking like "your profile"
            else: # If youre not looking foryourself..
                filter = Q(user_id = user_id) # Filter ideas by the requested user id
                if ConnectionRequest.is_followed(user.id, user_id):
                    filter = filter & ~Q(visibility=Idea.Visibility.private.value) # Public and protected ones, because the user has accepted the logged user connection
                else:
                    filter = filter & Q(visibility=Idea.Visibility.public.value) # Or just only the public because the users are not "friends" (or still not accepted)
                    
                res_ideas = Idea.objects.filter(filter).order_by('-created_at')
            
            return res_ideas
        else:
            raise Exception('Not logged in!')
        
    def resolve_timeline(root, info, **kwargs):
        """Returns all the ideas from follow users + user ideas.
        """
        user = info.context.user
        if not user.is_anonymous:
            filter = Q(user_id = user.id) # Self ideas
                                            # + follow user ideas public and protected (no privates)
            return Idea.objects.filter(filter).order_by('-created_at')
        else:
            raise Exception('Not logged in!')
