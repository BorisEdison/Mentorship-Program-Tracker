from django.urls import path
from requests import request
from . import views


urlpatterns = [
    path('ScheduleMeet', views.HomeView.as_view(), name='Schedule'),
    path('calender', views.Open_Faculty_Cal, name='faculty-cal'),
    path('calendar', views.Open_Student_Cal, name='student-cal'),
]
