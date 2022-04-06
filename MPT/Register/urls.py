
from django.urls import path
from . import views


urlpatterns = [
    path('RegisterPage', views.user, name= 'register'),
    path('LoginPage', views.login, name= 'Login'),
    path("logout", views.logout, name="logout"),
]
