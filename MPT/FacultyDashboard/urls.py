from django.urls import path, include
from . import views


urlpatterns = [
    path('facultydashboard/<str:pk>', views.faculty, name= 'faculty'),
    path('facultydashboard/<str:fac_id>/student/<str:stu_id>/', views.studentdetail, name= 'studentdetail'),
    path('logout/', views.logout, name= 'logout'),
    path('facultyMeeting', views.facultyMeeting, name='faculty-meeting'),    
    path('overallMeetingRecords', views.overallMeetingRecords, name='overall-meeting-records'),    
    path('deleteMeeting/<str:id>', views.deleteMeeting, name='delete-meeting-record'),
    path('faculty/induvidualMeetingRecords/<str:fac_id>/<str:stu_id>/', views.induvidualMeetingRecords, name='induvidual-meeting-records'),  
    path('meetingNotes/<str:id>', views.meetingNotes, name='meeting-notes'),       
    #faculty accessing notes from student dashboard (individual meeting records)
    path('faculty/induvidualMeetingRecords/<str:fac_id>/student/<str:stu_id>/meetingNotes/<str:meet_id>', views.individualMeetingNotes, name='individual-meeting-notes'),
    path('faculty/induvidualMeetingRecords/<str:fac_id>/student/<str:stu_id>/deleteMeetingNotes/<str:meet_id>/', views.individualDeleteMeeting, name='individual-delete-meeting-record'),
]
