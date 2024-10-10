from django.urls import path
from . import views

# Define URL patterns for login and logout views
urlpatterns = [
    # Login page
    path('login', views.login, name='login'),
    
    # Logout page
    path('logout/', views.logout, name='logout'),
]
