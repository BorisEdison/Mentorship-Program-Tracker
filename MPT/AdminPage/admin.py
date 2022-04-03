from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

Desc = 'Add College Email-ID'
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('username','email', 'first_name', 'is_active', 'is_staff')
    ordering = ('email',)
    list_display = ('username','email', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('Section 1', {'fields': ('email', 'first_name', 'last_name',),  
                       'description': '%s' % Desc,
        
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active'),
                         'classes': ('collapse',),
        }),
       
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

class Admin(admin.AdminSite):
    site_header = 'MPT'

# admin.site.unregister(User)

admin_site = Admin(name='MPTAdmin')
admin_site.register(User,UserAdminConfig)