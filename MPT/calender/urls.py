from django.urls import path
from . import views


urlpatterns = [
    path('Calender', views.Open_Cal, name='Cal'),
]
