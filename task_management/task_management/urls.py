"""
URL configuration for task_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login', permanent=False)),  # Redirect root URL to login
    path('', include('authenticate.urls')),  # Include your authenticate app URLs
    path('tasks/', include('tasks.urls')),
    path('openai/', include('open_ai.urls'), name='openai'),
    path('docs/', serve, {'path': 'build/latex/taskmanagementsystem.pdf', 'document_root': os.path.join(settings.BASE_DIR, 'docs')}, name='documentation'),  # Serve the PDF
]

# Serve static files during development (not recommended for production)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)