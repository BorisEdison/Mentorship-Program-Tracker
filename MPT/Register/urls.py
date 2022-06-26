from django.urls import path
from . import views


urlpatterns = [
    path('Sign-Up', views.StudentRegister, name='register'),
    path('Add-Faculty', views.FacultyRegister, name='FacultyRegister'),
    path('Add-Admin', views.AdminRegister, name='AdminRegister'),
]
