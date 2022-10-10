from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from Announcement.models import *
from FacultyDashboard.models import *
# importing Student
from accounts.models import (
    StudentProfile, 
    StudentDetails, 
    StudentContactDetail, 
    StudentHobbies, 
    GuardianDetails, 
    StudentExtraCurricular, 
    StudentMedicalReport,)
# importing Mentor
from accounts.models import MentorProfile,Mentor_assign
from accounts.models import User
from Marks.models import AcademicScores,SemCGPA
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

Desc = 'Add College Email-ID'

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=User
    list_display=('email','usr_id','is_staff','is_active','is_superuser',)
    list_filter=('email','usr_id','is_staff','is_active','is_superuser',)
    fieldsets = (
        (None, {
            "fields": (
                'email','usr_id','password','first_name','last_name','phone','profile_img',
            ),
        }),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_superuser',),
            'classes': ('collapse',),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['first_name'].required = False
        form.base_fields['last_name'].required = False
        form.base_fields['phone'].required = False
        form.base_fields['profile_img'].required = False
        return form

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            "fields": (
                'email','password1','password2','usr_id','first_name','last_name','phone','profile_img','is_staff','is_active','is_superuser',
            ),
        }),
    )
    
    
    search_fields=('email','usr_id',)
    ordering=('email','usr_id',)

  
# class UserAdminConfig(UserAdmin):
#     model = User
#     search_fields = ('email', 'user_name', 'first_name',)
#     list_filter = ('username','email', 'first_name', 'is_active', 'is_staff')
#     ordering = ('email',)
#     list_display = ('username','email', 'first_name',
#                     'is_active', 'is_staff')
#     fieldsets = (
#         ('Section 1', {'fields': ('email', 'first_name', 'last_name',),  
#                        'description': '%s' % Desc,
        
#         }),
#         ('Permissions', {'fields': ('is_staff', 'is_active'),
#                          'classes': ('collapse',),
#         }),
       
#     )
    
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )

class Admin(admin.AdminSite):
    site_header = 'MPT'

# admin.site.unregister(User)

admin_site = Admin(name='MPTAdmin')
# admin_site.register(User,UserAdminConfig)
admin_site.register(User,CustomUserAdmin)
admin_site.register(StudentProfile)
admin_site.register(StudentDetails)
admin_site.register(StudentContactDetail)
admin_site.register(StudentHobbies)
admin_site.register(GuardianDetails)
admin_site.register(StudentExtraCurricular)
admin_site.register(StudentMedicalReport)
admin_site.register(MentorProfile)
admin_site.register(Mentor_assign)
admin_site.register(AcademicScores)
admin_site.register(SemCGPA)   
admin_site.register(Announcement)
admin_site.register(AnnouncementReceiver)
admin_site.register(Meeting)
admin_site.register(MeetingAttendance)