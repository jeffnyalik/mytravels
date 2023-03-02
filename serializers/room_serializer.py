from rest_framework import serializers
from serializers.roomtype_serializer import *
from hotels.hotel_model import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'price', 'hotel', 'image']
