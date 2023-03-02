from django.db import models

class Flight(models.Model):
    airline_name = models.CharField(max_length=100, blank=True, null=True)
    flight_number = models.CharField(max_length=50, blank=True, null=True)
    arrival_airport = models.CharField(max_length=50, blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Flights"
        app_label = "api"
    
    def __str__(self) -> str:
        return self.airline_name
