from rest_framework import serializers
from flights.flight_model import *
from serializers.flight_serializer import *

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            "id",
            "airline_name",
            "arrival_airport",
            "departure_date",
            "arrival_date",
            "duration",
            "price"
        ]