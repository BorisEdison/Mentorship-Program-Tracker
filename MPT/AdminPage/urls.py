from django.urls import path
from . import views


urlpatterns = [
    # this is for student dashboard
    path('studentdashboard/<str:pk>', views.student, name= 'student'),

    # this is for admin page
    path('AdminPage', views.Adminpage, name= 'admin'),
    path('AdminPage/student', views.Adminstudent, name= 'admin-student'),
    path('AdminPage/mentor', views.Adminmentor, name= 'admin-mentor'),
    path('AdminPage/activity', views.Activity, name= 'admin-activity'),
    path('AdminPage/delete/<str:id>/',views.deleteuser, name= 'delete-user'),
    path('AdminPage/update/<str:usr_id>/',views.updateuserprofile, name= 'update-user'),
    ]
