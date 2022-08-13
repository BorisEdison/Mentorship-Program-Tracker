from django.urls import path
from . import views

urlpatterns = [
    path('Annoucement', views.announcement, name='faculty-announcement'),
]