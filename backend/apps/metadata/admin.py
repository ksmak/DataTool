from django.contrib import admin
from .models import (
    Department,
    Dictionary,
    Database,
    Form,
    Group,
    Field,
    Report,
    Converter
)


class DepartmentAdmin(admin.ModelAdmin):
    """Department admin"""

    list_display = (
        'title',
    )

    list_display_links = (
        'title',
    )


class DictionaryAdmin(admin.ModelAdmin):
    """Dictionary admin"""

    list_display = (
        'title',
        'table_name'
    )


class DatabaseAdmin(admin.ModelAdmin):
    """Database admin"""

    list_display = (
        'num',
        'title'
    )

    list_display_links = (
        'title',
    )


class FormAdmin(admin.ModelAdmin):
    """Form admin"""

    list_display = (
        'num',
        'db',
        'title',
        'form_type'
    )

    list_display_links = (
        'db',
        'title'
    )


class GroupAdmin(admin.ModelAdmin):
    """Group admin"""

    list_display = (
        'num',
        'form',
        'title',
        'is_multy',
        'table_name'
    )

    list_display_links = (
        'form',
        'title',
    )

    ordering = ('num', )


class FieldAdmin(admin.ModelAdmin):
    """Field admin"""

    list_display = (
        'num',
        'group',
        'title',
        'field_name',
        'field_type',
        'len',
        'is_key',
        'is_visible',
        'is_enable',
        'is_require',
        'precision',
        'is_duplicate'
    )

    list_display_links = (
        'group',
        'title',
    )

    ordering = ('num', )


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Database, DatabaseAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Report)
admin.site.register(Converter)
