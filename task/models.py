from mongoengine import *

# Create your models here.
class Task(Document):
  name = StringField(required=True)
  logged_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)