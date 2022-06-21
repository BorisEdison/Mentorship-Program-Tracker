from django.urls import path
from . import views


urlpatterns = [
    path('AdminPage', views.Adminpage, name= 'admin'),
   
    path('studentdashboard/<str:pk>', views.student, name= 'student'),
    
    # path("ViewProfile", views.stud_prof, name="student-profile")
]
