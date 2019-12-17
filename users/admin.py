from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['id', 'email', 'username', 'age']
    list_display_links = ['id', 'email', 'username']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
