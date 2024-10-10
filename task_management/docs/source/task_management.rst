task_management package
========================

The `task_management` package serves as the main entry point for the task management project. It includes all the configurations, routing, and settings necessary for the application to function properly.

Submodules
----------

task_management.asgi module
----------------------------
This module handles ASGI configurations for the Django application, enabling support for asynchronous features like WebSockets.

.. automodule:: task_management.asgi
   :members:
   :undoc-members:
   :show-inheritance:

task_management.consumers module
---------------------------------
Contains WebSocket consumers that handle real-time communication for the application, such as notifying users about task updates.

.. automodule:: task_management.consumers
   :members:
   :undoc-members:
   :show-inheritance:

task_management.routing module
-------------------------------
Defines the routing for WebSocket connections, mapping channels to consumers.

.. automodule:: task_management.routing
   :members:
   :undoc-members:
   :show-inheritance:

task_management.settings module
-------------------------------
This module contains all the project settings for Django, including database configurations, middleware settings, installed applications, and more.

.. automodule:: task_management.settings
   :members:
   :undoc-members:
   :show-inheritance:

task_management.urls module
----------------------------
This module handles URL routing for the task management project.

The `urlpatterns` list routes URLs to the appropriate views within the application. Below are the main routes configured:

- **Admin Interface**: Accessible at `/admin/`, providing admin functionalities for managing the application.
- **Root URL**: Redirects to the login page, accessible at `/`, which is set up using `RedirectView`.
- **Authentication URLs**: Routes for authentication views, such as login and logout, handled in the `authenticate` app.
- **Tasks URLs**: Routes for task-related functionalities, such as creating, updating, and deleting tasks, managed in the `tasks` app.
- **OpenAI URLs**: Routes for integrating OpenAI functionalities, handled in the `open_ai` app.

.. automodule:: task_management.urls
   :members:
   :undoc-members:
   :show-inheritance:

task_management.wsgi module
----------------------------
This module provides the entry point for WSGI-compatible web servers to serve your project. It is typically used for deployment.

.. automodule:: task_management.wsgi
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: task_management
   :members:
   :undoc-members:
   :show-inheritance:
