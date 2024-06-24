from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_uuid = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    label = models.CharField(max_length=100)
