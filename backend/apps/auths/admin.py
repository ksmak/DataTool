from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Role, UserRole, DatabaseAccess, FormAccess


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


class UserRoleAdmin(admin.ModelAdmin):
    """UserRole admin"""
    list_display = ('user', 'role')
    list_display_links = ('user', 'role')


class DatabaseAccessAdmin(admin.ModelAdmin):
    """DatabaseAccess admin"""
    list_display = ('role', 'database')
    list_display_links = ('role', 'database')


class FormAccessAdmin(admin.ModelAdmin):
    """FormAccess admin"""
    list_display = ('role', 'form', 'access_type')
    list_display_links = ('role', 'form', 'access_type')


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Role)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(DatabaseAccess, DatabaseAccessAdmin)
admin.site.register(FormAccess, FormAccessAdmin)
