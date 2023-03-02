from rest_framework import serializers
from hotels.hotel_model import *

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name', 'description']

