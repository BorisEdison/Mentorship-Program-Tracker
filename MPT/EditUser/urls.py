from django.urls import path
from . import views

urlpatterns = [
    path('EditPage/', views.edit, name="Edit")
]
