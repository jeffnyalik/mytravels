from django.contrib import admin
from .models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']

admin.site.register(Supplier, SupplierAdmin)