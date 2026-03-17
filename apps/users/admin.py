from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm

from apps.users.models import User


class CustomUserChangeForm(UserChangeForm):
    """
    Custom user change form class
    """

    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            'using <a href="{}">this form</a>.'
        ),
    )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom UserAdmin class
    """

    form = CustomUserChangeForm
    readonly_fields = ("id", "date_joined", "last_login")
    fieldsets = (
        ("Login", {"fields": ("email", "password")}),
        (
            "Data",
            {
                "fields": (
                    "id",
                    "name",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password1", "password2", "is_staff", "is_superuser"),
            },
        ),
    )
    list_display = ("email", "is_staff", "date_joined", "last_login")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "name")
    ordering = ("date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
