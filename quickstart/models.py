from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    dueDate = models.DateField()
    priority = models.TextField()
    completed = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    section = models.CharField(max_length=100, default="In Progress")