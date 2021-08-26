import graphene
from .types import Query as IdeaQuery

class Query(IdeaQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)