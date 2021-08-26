import graphene
from ideas.schema import schema as IdeaSchema
from users.schema import schema as UserSchema

class Query(IdeaSchema.Query, UserSchema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)