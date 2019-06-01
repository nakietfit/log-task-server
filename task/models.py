from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
  name = models.TextField(blank=True)
  logged_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)