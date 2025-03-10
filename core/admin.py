from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
  model = CustomUser
  list_display = ['email','username','user_type','is_staff']
  list_filter = ['is_staff','is_active']
  fieldsets = (
    (None, {'fields': ('email', 'username', 'password')}),
    ('Personal_Info', {'fields': ('user_type','address','phone_number')}),
    ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','groups','user_permissions')}),
    ('Important_dates', {'fields': ('last_login',)}),  # Removed 'date_joined' from here
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email','username','password1','password2','user_type','is_staff','is_active')
    }),
  )
  search_fields = ['email','username']
  ordering = ['email']
admin.site.register(CustomUser, CustomUserAdmin)
