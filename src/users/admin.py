from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "email", "username", "birth_date", "gender")},
        ),
        (_("Phone"), {"fields": ("phone_number", "phone_confirm", "phone_region")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("password1", "password2"),
            },
        ),
    )
    list_display = ["email", "username", "phone_number", "is_superuser", "is_active"]
    search_fields = ["first_name", "last_name", "phone_number", "email"]
    ordering = ("-created",)
