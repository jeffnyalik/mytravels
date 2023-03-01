from django.contrib import admin
from .models import *

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']

admin.site.register(Supplier, SupplierAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']

admin.site.register(Customer, SupplierAdmin)