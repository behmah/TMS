authenticate package
====================

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   authenticate.migrations

Submodules
----------

authenticate.admin module
-------------------------

.. automodule:: authenticate.admin
   :members:
   :undoc-members:
   :show-inheritance:

authenticate.apps module
------------------------

.. automodule:: authenticate.apps
   :members:
   :undoc-members:
   :show-inheritance:

authenticate.models module
--------------------------

.. automodule:: authenticate.models
   :members:
   :undoc-members:
   :show-inheritance:

authenticate.urls module
------------------------

This module defines the URL patterns for the authentication views.

.. http:get:: /login

   Maps to the `login` view. Handles user authentication via POST request and renders the login page on GET.

   **Returns**:
       - On successful login, redirects to the home page.
       - On failure, renders the login form with an error message.

.. http:get:: /logout/

   Maps to the `logout` view. Logs the user out and redirects to the login page.

authenticate.views module
-------------------------

.. automodule:: authenticate.views
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: authenticate
   :members:
   :undoc-members:
   :show-inheritance:
