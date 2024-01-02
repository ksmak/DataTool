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


class CountriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_enable',
    )



class NationalsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_enable',
    )



class RegistrationstateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'is_enable',
    )



class AsbAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'surname',
        'name',
        'patronymic',
        'birth_date',
        'iin',
        'citizen',
        'nation',
    )



class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'region',
        'district',
        'punkt',
        'status',
        'registration_date',
    )

admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Nationals, NationalsAdmin)
admin.site.register(Registrationstate, RegistrationstateAdmin)
admin.site.register(Asb, AsbAdmin)
admin.site.register(Address, AddressAdmin)

