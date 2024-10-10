
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.core.cache import cache
from django.contrib import messages
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Task
from .serializers import TaskSerializer


CACHE_TIMEOUT = 60 * 15  # 15 minutes
CACHE_KEY = "index_page_cache_key"

def index(request):
    """
    Displays the list of tasks.

    If the request method is GET, retrieves tasks from the cache or database
    and renders the index.html template with the tasks data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the index.html template with the tasks.
    """
    if request.method == 'GET':
        # Try to get the cached data first
        tasks = cache.get(CACHE_KEY)
        # If cache is empty, fetch from database and set cache
        if not tasks:
            tasks = Task.objects.select_related('assigned_to').order_by('-created_at')
            serializer = TaskSerializer(tasks, many=True)
            tasks = serializer.data
            cache.set(CACHE_KEY, tasks, CACHE_TIMEOUT)  # Cache the data for 15 minutes
        
        return render(request, 'index.html', {'tasks': tasks})

@login_required
def create_task(request):
    """
    Handles the creation of new tasks.

    If the request method is POST, validates and saves the new task. 
    It also invalidates the cache and notifies WebSocket clients about the new task.
    
    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the tasks index page on success, or re-renders 
                      the create task form with error messages on failure.
    """
    users = User.objects.all()
    if request.method == 'POST':
        try:
            data = request.POST
            task_serializer = TaskSerializer(data=data)
            if task_serializer.is_valid():
                task = task_serializer.save()
                # Invalidate cache after task creation

                # Notify WebSocket clients about the new task
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "tasks",  
                    {
                        "type": "task_message",
                        "message": f"New Task '{task.title}' created by {request.user.username}",
                    }
                )
                cache.delete(CACHE_KEY)
                return redirect(reverse('tasks'))
            else:
                return render(request, 'create.html', {'errors': task_serializer.errors, 'users': users})
        except Exception as e:
            return render(request, 'create.html', {'error': str(e), 'users': users})
    else:
        return render(request, 'create.html', {'users': users})

@login_required
def update_task(request, id):
    """
    Handles the update of an existing task.

    Retrieves the task by ID and renders the update form. If the request method is POST,
    validates and saves the updated task data. Informs WebSocket clients about the task update.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the task to be updated.

    Returns:
        HttpResponse: Redirects to the tasks index page on successful update,
                      or re-renders the update form with error messages on failure.
    """
    try:
        task = get_object_or_404(Task, pk=id)  # Fetch the task by ID
        users = User.objects.all()  # Get all users for the assigned_to dropdown
        if request.method == 'GET':
            # Render the update form with the task's current data
            return render(request, 'update.html', {'task': task, 'users': users})
        elif request.method == 'POST':
            # Handle form submission and update the task
            data = request.POST
            task_serializer = TaskSerializer(task, data=data, partial=True)  # Use partial to allow partial updates
            if task_serializer.is_valid():
                task_serializer.save()

                # Notify WebSocket clients about the updated task
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "tasks",  
                    {
                        "type": "task_message",
                        "message": f"Task '{task.title}' updated by {request.user.username}",
                    }
                )
                cache.delete(CACHE_KEY)
                # Redirect to the task list page on successful update
                return redirect(reverse('tasks'))
            else:
                # If the form is invalid, re-render the page with error messages
                return render(request, 'update.html', {'errors': task_serializer.errors, 'users': users})
    except Task.DoesNotExist:
        # If task not found, redirect with an error message
        messages.error(request, "Task not found.")
        return redirect(reverse('tasks'))

@login_required
def delete_task(request, id):
    """
    Handles the deletion of a task.

    Checks if the user has permission to delete the task. If the task is found, 
    it deletes the task and invalidates the cache. If the task does not exist, 
    or the user lacks permissions, it returns an appropriate error message.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the task to be deleted.

    Returns:
        HttpResponse: Redirects to the tasks index page after deletion or 
                      shows an error message if deletion fails.
    """
    # Check if the user is a superuser
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete this task.")
        return redirect(reverse('tasks'))

    try:
        task = Task.objects.get(pk=id)
        task.delete()
        cache.delete(CACHE_KEY)
        return redirect(reverse('tasks'))
    except Task.DoesNotExist:
        messages.error(request, "Task not found.")
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
