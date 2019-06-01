import graphene
from graphene_django import DjangoObjectType
from .models import Task
from user.schema import UserType

class TaskType(DjangoObjectType):
  class Meta:
    model = Task

class Query(graphene.ObjectType):
  tasks = graphene.List(TaskType)

  def resolve_tasks(self, info, **kwargs):
    return Task.objects.all()

class CreateTask(graphene.Mutation):
  id = graphene.Int()
  name = graphene.String()
  logged_by = graphene.Field(UserType)

  class Arguments:
    name = graphene.String()

  def mutate(self, info, name):
    user = info.context.user or None

    task = Task(
      name=name,
      logged_by=user,
    )
    task.save()

    return CreateTask(
      id=task.id,
      name=task.name,
      logged_by=task.logged_by,
    )

class Mutation(graphene.ObjectType):
  create_task = CreateTask.Field()