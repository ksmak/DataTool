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


class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_enable',
    )



class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )



class AsbAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )

admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Asb, AsbAdmin)

