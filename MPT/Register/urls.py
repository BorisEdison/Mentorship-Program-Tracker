from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('Sign-Up', views.StudentRegister, name='register'),
    path('Add-Faculty', views.FacultyRegister, name='FacultyRegister'),
    path('Add-Admin', views.AdminRegister, name='AdminRegister'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    # Reset Password urls
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'Register/password_reset_form.html', success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name='Register/password_reset.html',success_url=reverse_lazy('password_reset_done'), email_template_name='Register/forgot_password_email.html'),name='reset_password'),
    path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(template_name='Register/password_reset_done.html'),name='password_reset_done'),
    path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Register/password_reset_complete.html'),name='password_reset_complete'),

    # path('reset-view/',views.reset_view,name='reset_view'),
]
