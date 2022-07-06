from django.urls import path
from . import views


urlpatterns = [
     path('studentdashboard/<str:pk>/marks', views.studentMarks, name= 'studentMarks'),
]

