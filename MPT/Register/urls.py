from django.urls import path
from . import views


urlpatterns = [
    path('Sign-Up', views.user, name='register'),
    path("logout", views.logout, name="logout"),
]
