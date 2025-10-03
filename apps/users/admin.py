from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # This class inherits from UserAdmin to provide all the default
    # fields and functionality for the admin interface.
    pass
