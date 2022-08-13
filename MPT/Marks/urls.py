from django.urls import path
from . import views


urlpatterns = [
     path('studentdashboard/<str:pk>/marks', views.studentMarks, name= 'studentMarks'),
     path('faculty/<str:stu_pk>/marks', views.facultyStudentMarks, name= 'facultyStudentMarks'),
     path('faculty/<str:stu_pk>/marks/add', views.facultyAddMarks, name= 'facultyAddMarks'),
     path('faculty/<str:stu_pk>/marks/edit', views.facultyEditMarks, name= 'facultyEditMarks'),

]

