from django.urls import path
from . import views

urlpatterns = [
    path('facultyAnnoucement', views.facultyAnnouncement, name='faculty-announcement'),    
    path('facultyAnnoucementNew', views.facultyAnnouncementNew, name='faculty-announcement-new'),
    path('studentAnnoucement', views.studentAnnouncement, name='student-announcement'),
    path('delete/<str:id>/',views.deleteAnnouncement, name= 'delete-announcement'),
]