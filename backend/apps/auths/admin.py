from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


class MyUserAdmin(UserAdmin):
    """MyUser admin"""

    list_display = (
        'username',
        'first_name',
        'last_name',
        'middle_name',
        'department',
        'is_active'
    )

    list_display_links = (
        'username',
    )

    readonly_fields = (
        'is_superuser',
    )

    fieldsets = (
        ('Personal', {
            'classes': (
                'wide',
            ),
            'fields': (
                'username',
                'password',
                'first_name',
                'last_name',
                'middle_name',
                'department',
            )
        }),
        ('Permissions', {
            'classes': (
                'wide',
            ),
            'fields': (
                'is_active',
                'is_staff',
                'groups',
                'is_superuser',
            )
        }),
    )

    add_fieldsets = (
        ('Personal', {
            'classes': (
                'wide',
            ),
            'fields': (
                'username',
                'first_name',
                'last_name',
                'middle_name',
                'department',
            )
        }),
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'password1',
                'password2',
            )
        })
    )

    search_fields = ('username', )
    ordering = ('username', )


admin.site.register(MyUser, MyUserAdmin)
