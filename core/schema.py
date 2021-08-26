import graphene
from ideas.schema import schema as IdeaSchema
from users.schema import schema as UserSchema

class Query(IdeaSchema.Query, UserSchema.Query, graphene.ObjectType):
    pass

class Mutation(IdeaSchema.Mutation, UserSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)