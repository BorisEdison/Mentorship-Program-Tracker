from django.urls import path, include
from . import views


urlpatterns = [
    path('facultydashboard/<str:pk>', views.faculty, name= 'faculty'),
    path('facultydashboard/student/<str:pk>/', views.studentdetail, name= 'studentdetail'),
    path('logout/', views.logout, name= 'logout'),
    # path('/', include('EditUser.urls')),    

]
