# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# Use get_user_model to get the CustomUser model
CustomUser = get_user_model()

# Define a custom UserAdmin class to configure the display of CustomUser in the admin panel
class CustomUserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These fields are used when creating a user in the admin panel.
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
    
    # Fields to be displayed when viewing a user's details
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Fields to be displayed when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

# Register the CustomUser model with the custom admin interface
admin.site.register(CustomUser, CustomUserAdmin)

# Unregister the default Group model to exclude it from the admin panel
admin.site.unregister(Group)

