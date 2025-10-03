from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Add 'tenant' to the list of fields shown on the user list page
    list_display = UserAdmin.list_display + ("tenant",)

    # Add 'tenant' to the fields displayed on the user detail/edit page
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("tenant",)}),)

    # Add 'tenant' to the fields displayed when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("tenant",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
