from django.urls import path
from . import views


urlpatterns = [
    path('AdminPage', views.Adminpage, name= 'admin'),
    path('facultydashboard', views.faculty, name= 'faculty'),
    path('studentdashboard', views.student, name= 'student'),
    path('facultydashboard/<str:pk>/', views.studentdetail, name= 'studentdetail'),
    # path('EditPage/<str:pk>/', EditView.as_view(), name="Edit"),
    # path('EditPage/', views.edit, name="Edit"),
    path("ViewProfile", views.stud_prof, name="student-profile")
]
