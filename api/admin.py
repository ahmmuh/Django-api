from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

from . models import Activities
# Register your models here.
admin.site.register(Activities)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Profile', {'fields': ('email', 'first_name', 'last_name', 'profile_image',)}),
        ('Other stuff', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        
    )

admin.site.register(CustomUser, CustomUserAdmin)