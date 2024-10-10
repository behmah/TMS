tasks package
=============

The `tasks` package handles all functionalities related to task management within the application. This includes task creation, updating, deletion, and representation.

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   tasks.migrations

Submodules
----------

tasks.admin module
------------------
This module contains the admin configuration for managing tasks within the Django admin interface.

.. automodule:: tasks.admin
   :members:
   :undoc-members:
   :show-inheritance:

tasks.apps module
-----------------
This module contains the application configuration for the tasks app.

.. automodule:: tasks.apps
   :members:
   :undoc-members:
   :show-inheritance:

tasks.models module
-------------------
This module defines the `Task` model which represents tasks within the application.

.. automodule:: tasks.models
   :members:
   :undoc-members:
   :show-inheritance:

tasks.serializers module
------------------------
This module contains serializers for converting `Task` model instances to JSON format and vice versa.

.. automodule:: tasks.serializers
   :members:
   :undoc-members:
   :show-inheritance:

tasks.urls module
-----------------
This module defines the URL patterns for the tasks app.

The `urlpatterns` list routes URLs to views. Below are the main routes configured:

- **/**: Maps to the `index` view which lists all tasks.
- **/create_task/**: Maps to the `create_task` view for creating new tasks.
- **/update_task/<int:id>**: Maps to the `update_task` view for editing existing tasks.
- **/delete_task/<int:id>**: Maps to the `delete_task` view for removing tasks.

.. automodule:: tasks.urls
   :members:
   :undoc-members:
   :show-inheritance:

tasks.views module
------------------
This module contains the view functions for handling requests related to tasks.

.. automodule:: tasks.views
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: tasks
   :members:
   :undoc-members:
   :show-inheritance:
