from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('register/', views.register_child, name='register_child'),  # Register URL
    path('check-in/', views.check_in_child, name='check_in_child'),  # Correctly reference check_in_child
]
