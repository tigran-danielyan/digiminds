from django.contrib.auth.models import User
from django.db import models

from tasks.enumeration import TaskStatus


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=256)
    # status = models.IntegerField(choices=TaskStatus)
