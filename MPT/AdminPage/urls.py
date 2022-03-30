
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Adminpage, name= 'admin'),
]
