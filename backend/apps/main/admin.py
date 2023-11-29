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


class DictionaryAdmin(admin.ModelAdmin):
    """Dictionary admin"""

    list_display = (
        'title',
        'table_name'
    )


class GroupAdmin(admin.ModelAdmin):
    """Group admin"""

    list_display = (
        'title',
        'is_multy',
        'table_name'
    )


class FieldAdmin(admin.ModelAdmin):
    """Field admin"""

    list_display = (
        'order',
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
        'field_type',
    )

    ordering = ('order', )


admin.site.register(Department)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Database)
admin.site.register(Form)
admin.site.register(Group)
admin.site.register(Field, FieldAdmin)
admin.site.register(Report)
admin.site.register(Converter)
