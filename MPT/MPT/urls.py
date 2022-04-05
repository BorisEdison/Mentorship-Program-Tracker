
from django.contrib import admin
from django.urls import path, include
from AdminPage.admin import admin_site
from Register import views

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('AdminPage.urls')),
    path('',views.login),
    path('', include('Register.urls')),

]


