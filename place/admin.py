from django.contrib import admin
from .models import Country, State


# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'phone_code', 'capital', 'currency', 'region', 'is_active', 'created_at')
    fields = ('country_name', 'phone_code', 'capital', 'currency', 'region', 'is_active')
    readonly_fields = ('created_at', )
    list_editable = ['is_active']
    search_fields = ['country_name']


admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('country', 'state_name', 'state_code', 'is_active', 'created_at')
    fields = ('country', 'state_name', 'state_code', 'is_active')
    readonly_fields = ('created_at', )
    list_editable = ['is_active']
    search_fields = ['state_name']


admin.site.register(State, StateAdmin)
