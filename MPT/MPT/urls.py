
from django.contrib import admin
from django.urls import path, include
from AdminPage.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('AdminPage.urls')),
    path('user/', include('Register.urls'))
]


