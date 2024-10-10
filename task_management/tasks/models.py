from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    """
    Represents a task in the task management system.

    Attributes:
        title (str): The title of the task.
        description (str, optional): A detailed description of the task.
        due_date (datetime, optional): The date and time by which the task should be completed.
        assigned_to (User): The user to whom the task is assigned.
        status (str): The current status of the task (Todo, Doing, Review, Done).
        created_at (datetime): The date and time when the task was created.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=50, choices=[('todo', 'Todo'), ('doing', 'Doing'), ('review','Review'), ('done', 'Done')])
    created_at = models.DateTimeField(auto_now_add=True)
