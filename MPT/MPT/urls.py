
from django.contrib import admin
from django.urls import path, include
from AdminPage.admin import admin_site


urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('AdminPage.urls')),
    path('', include('Register.urls')),
    path('', include('Login.urls')),    
    path('edit/', include('EditUser.urls')),    
    path('', include('FacultyDashboard.urls')),    
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)