from django.urls import path
from . import views


urlpatterns = [
    path('facultydashboard/<int:pk>', views.faculty, name= 'faculty'),
    path('facultydashboard/student/<str:pk>/', views.studentdetail, name= 'studentdetail'),
]
