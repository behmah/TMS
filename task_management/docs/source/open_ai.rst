open_ai package
================

The `open_ai` package handles interactions with the OpenAI API and provides views for processing user inputs.

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   open_ai.migrations

Submodules
----------

open_ai.admin module
---------------------
This module is responsible for registering the OpenAI models and any other related components in the Django admin interface.

.. automodule:: open_ai.admin
   :members:
   :undoc-members:
   :show-inheritance:

open_ai.apps module
--------------------
Contains the configuration for the OpenAI app, including app-specific settings.

.. automodule:: open_ai.apps
   :members:
   :undoc-members:
   :show-inheritance:

open_ai.ollama_phi module
---------------------------
This module defines the function to interact with the Ollama Phi3 model. It includes methods for sending user input and receiving responses.

.. automodule:: open_ai.ollama_phi
   :members:
   :undoc-members:
   :show-inheritance:

open_ai.urls module
--------------------
This module defines the URL patterns for the OpenAI app views.

.. http:get:: /chatphi/
   Maps to the `chatphi` view. This view handles user input and returns a response from the Ollama Phi3 model.

   **Returns**:
       - Renders the `ollama_phi.htm` template with the model's response if the request method is POST.
       - Renders the same template for GET requests without a user input.

.. automodule:: open_ai.urls
   :members:
   :undoc-members:
   :show-inheritance:

open_ai.views module
---------------------
This module contains views for processing user input and interacting with the OpenAI API.

.. http:get:: /chatphi/
   Renders the chat interface for interacting with the Ollama Phi model.

   **Returns**:
       - Renders the `ollama_phi.htm` template with the model's response if a POST request is made with user input.
       - Renders the same template without a response for GET requests.

.. automodule:: open_ai.views
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: open_ai
   :members:
   :undoc-members:
   :show-inheritance:
