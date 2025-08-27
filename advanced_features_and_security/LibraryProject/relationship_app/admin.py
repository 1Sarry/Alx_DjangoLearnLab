from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserProfile
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUserProfile
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUserProfile, CustomUserAdmin)