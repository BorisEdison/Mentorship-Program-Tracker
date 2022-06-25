from django.urls import path
from requests import request
from . import views


urlpatterns = [
    path('ScheduleMeet', views.HomeView.as_view(), name='Schedule'),
    path('Calender', views.Open_Cal, name='Cal'),
]
