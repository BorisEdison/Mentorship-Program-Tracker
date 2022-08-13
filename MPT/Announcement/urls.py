from django.urls import path
from . import views

urlpatterns = [
    path('facultyAnnoucement', views.facultyAnnouncement, name='faculty-announcement'),
    path('studentAnnoucement', views.studentAnnouncement, name='student-announcement'),
]