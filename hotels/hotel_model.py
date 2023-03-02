from django.db import models
from uuid import uuid4
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid4().hex}.{ext}"
        return f"{self.path}/{filename}"

hotel_image_path = PathAndRename("hotels_images")
room_image_path = PathAndRename("rooms_images")

class RoomType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        app_label = "api"
        verbose_name_plural = "Room Types"

    def __str__(self):
        return self.name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    checkin_date = models.DateField(blank=True, null=True)
    checkout_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    image = models.ImageField(upload_to=hotel_image_path)

    def __str__(self) -> str:
        return self.hotel_name

    class Meta:
        app_label = "api"
        verbose_name_plural = "Hotels"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, null=True)
    room_number = models.CharField(max_length=50, blank=True, null=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=1, blank=True, null=True)
    check_in_date = models.DateField(blank=True, null=True)
    check_out_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to=room_image_path)

    class Meta:
        app_label = "api"
        verbose_name_plural = "Rooms"

    def __str__(self) -> str:
        return f"Room {self.room_number} at {self.hotel.hotel_name}"
