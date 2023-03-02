from django.contrib import admin
from .models import *

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']

admin.site.register(Supplier, SupplierAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'address', 'city', 'country')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hotel', 'room_type', 'price')

admin.site.register(Customer, SupplierAdmin)