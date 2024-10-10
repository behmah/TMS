from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tasks'),  # Route for the task index page
    path('create_task/', views.create_task, name='create_task'),  # Route for creating a new task
    path('update_task/<int:id>', views.update_task, name='update_task'),  # Route for updating a task by ID
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),  # Route for deleting a task by ID
]
"""
URL patterns for the tasks app.

Routes:
    - / : Maps to the `index` view which lists all tasks.
    - /create_task/ : Maps to the `create_task` view for creating new tasks.
    - /update_task/<int:id> : Maps to the `update_task` view for editing existing tasks.
    - /delete_task/<int:id> : Maps to the `delete_task` view for removing tasks.
"""
