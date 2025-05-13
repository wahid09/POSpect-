from django.contrib import admin
from .models import Suppliers, Customer, Warehouse


# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'name', 'email', 'phone_number', 'is_active', 'created_at')
    fields = ('country', 'state', 'name', 'email', 'phone_number', 'address', 'description', 'is_active')
    list_editable = ['is_active']
    search_fields = ['name']


admin.site.register(Suppliers, SupplierAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'name', 'email', 'phone_number', 'is_active', 'created_at')
    fields = ('country', 'state', 'name', 'email', 'phone_number', 'address', 'is_active')
    list_editable = ['is_active']
    search_fields = ['name']


admin.site.register(Customer, CustomerAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'name', 'email', 'phone_number', 'is_active', 'created_at')
    fields = ('country', 'state', 'name', 'email', 'phone_number', 'is_active')
    list_editable = ['is_active']
    search_fields = ['name']


admin.site.register(Warehouse, WarehouseAdmin)
