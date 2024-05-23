from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'cpf', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cpf',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('cpf',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)