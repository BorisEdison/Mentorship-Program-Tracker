from django.urls import path
from . import views
from .views import EditView

urlpatterns = [
    path('AdminPage', views.Adminpage, name= 'admin'),
    path('facultydashboard', views.faculty, name= 'faculty'),
    path('facultydashboard/<str:pk>/', views.studentdetail, name= 'studentdetail'),
    # path('EditPage/<str:pk>/', EditView.as_view(), name="Edit"),
    path('EditPage/', views.edit, name="Edit")
]
