
from django.urls import path
from . import views

urlpatterns = [
    path('RegisterPage', views.user, name= 'register'),
]
