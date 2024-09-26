# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # For Django admin
    path('', include('daycare.urls')),  # Includes URLs from the app "daycare"
]
