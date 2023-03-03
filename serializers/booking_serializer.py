from rest_framework import serializers
from bookings.booking_model import *
from serializers.room_serializer import *

class BookingSerizer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ('id', 'user', 'room', 'check_in', 'check_out', 'deposit_paid', 'paid_amount', 'balance')
