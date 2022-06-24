from django.urls import path
from . import views


urlpatterns = [
    path('Calender', views.HomeView.as_view(), name='Cal'),
]
