import graphene
import task.schema

class Query(task.schema.Query, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)