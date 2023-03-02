from rest_framework import serializers
from hotels.hotel_model import *
from serializers.room_serializer import *

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'state', 'country', 'price', 'image', 'rooms']