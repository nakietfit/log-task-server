import graphene
from graphene_django import DjangoObjectType
from .models import Task

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

  class Arguments:
    name = graphene.String()

  def mutate(self, info, name):
    task = Task(name=name)
    task.save()

    return CreateTask(
      id=task.id,
      name=task.name,
    )

class Mutation(graphene.ObjectType):
  create_task = CreateTask.Field()