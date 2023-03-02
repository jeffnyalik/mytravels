from rest_framework import serializers
from hotels.hotel_model import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'price', 'hotel', 'image']
