from django.db import models
from django.conf import settings
from hotels.hotel_model import Room

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    deposit_paid = models.BooleanField(default=False, blank=True, null=True)
    paid_amount = models.FloatField(null=True, blank=True)

    class Meta:
        app_label = "api"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.user.email} - {self.room} - {self.check_in} to {self.check_out}"
