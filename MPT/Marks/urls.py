from django.urls import path
from . import views


urlpatterns = [
     path('studentdashboard/<str:pk>/marks', views.studentMarks, name= 'studentMarks'),
     path('studentdashboard/<str:pk>/marks/add', views.studentAddMarks, name= 'studentAddMarks'),
     path('studentdashboard/<str:pk>/marks/add/cgpa', views.studentAddCGPA, name= 'studentAddCGPA'),
     path('studentdashboard/<str:pk>/marks/<str:id>/edit', views.studentEditMarks, name= 'studentEditMarks'),
     path('studentdashboard/<str:pk>/marks/<str:id>/delete', views.studentDeleteMarks, name= 'studentDeleteMarks'),
     path('faculty/<str:stu_pk>/marks', views.facultyStudentMarks, name= 'facultyStudentMarks'),
     path('faculty/<str:stu_pk>/marks/add', views.facultyAddMarks, name= 'facultyAddMarks'),
     path('faculty/<str:stu_pk>/marks/add/cgpa', views.facultyAddCGPA, name= 'facultyAddCGPA'),
     path('faculty/<str:stu_pk>/marks/<str:id>/edit', views.facultyEditMarks, name= 'facultyEditMarks'),
     path('faculty/<str:stu_pk>/marks/<str:id>/delete', views.facultyDeleteMarks, name= 'facultyDeleteMarks'),
]

