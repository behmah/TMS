from django.urls import path
from . import views

urlpatterns = [
    path('chatphi/', views.chatphi, name='chatphi'),
]
"""
URL patterns for the open_ai app.

Routes:
    - /chatphi/ : Maps to the `chatphi` view which handles user interactions with the phi3 model.

"""
