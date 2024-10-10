from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.urls import reverse

def login(request):
    """
    Handle user login.

    If the request method is POST, it attempts to authenticate the user with the provided
    username and password. On successful login, the user is redirected to the home page ('tasks').
    If authentication fails, an error message is displayed.

    Args:
        request (HttpRequest): The request object containing metadata about the request.

    Returns:
        HttpResponse: Renders the login page if the request is GET or if login fails.
        Redirect: Redirects to the home page on successful login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            auth_login(request, user)
            return redirect(reverse('tasks'))  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password.")  # Add error message

    return render(request, 'login.htm')  # Render the login page for GET requests


def logout(request):
    """
    Handle user logout.

    Logs the user out and redirects to the login page.

    Args:
        request (HttpRequest): The request object containing metadata about the request.

    Returns:
        Redirect: Redirects to the login page after logout.
    """
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout
