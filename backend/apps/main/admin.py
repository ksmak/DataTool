from django.contrib import admin
from .models import *


class DocumentsAdmin(admin.ModelAdmin):
    list_display = (
        'is_active',
        'old_id',
        'date_start',
        'date_end',
        'created_at',
        'created_user',
        'changed_at',
        'changed_user'
)


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_enable',
    )



class AsbAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'vt',
        'dt',
        'p1',
        'country',
        'age',
        'im',
        'fam',
    )

admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Asb, AsbAdmin)

