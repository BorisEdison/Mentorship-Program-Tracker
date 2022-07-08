from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='Login'),
    path('Change-Password/', views.change_password, name='ChangePassword'),
]
