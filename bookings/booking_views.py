from serializers.booking_serializer import *
from bookings.booking_model import *
from rest_framework import generics
from custom_permissions.permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db import transaction
from decimal import Decimal, ROUND_HALF_UP


class ListBookingsApiView(generics.ListAPIView):
    serializer_class = BookingSerizer
    queryset = Booking.objects.all()
    # permission_classes = [IsCustomer]



class BookingApiView(generics.CreateAPIView):
    serializer_class = BookingSerizer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        user = self.request.user
        if user.IsCustomer:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)
        
    @transaction.atomic
    def create(self, request, room_id, hotel_id, *args, **kwargs):
        try:
            hotel = get_object_or_404(Hotel, id=hotel_id)
            room = get_object_or_404(Room, id=room_id, hotel=hotel)
            percentage = get_object_or_404(Percentage, hotel=hotel)
            
        except Room.DoesNotExist:
            return Response({'message': 'Room does not exist in this hotel.'}, status=status.HTTP_404_NOT_FOUND)
        if room.is_booked:
            return Response({'message': 'This room is already booked.'}, status=status.HTTP_400_BAD_REQUEST)

        room.is_booked = True
        room.save()
    

        # Calculate paid amount and round off to 2 decimal places
        paid_amount = round(room.price * Decimal(percentage.value) / Decimal('100.0'), 2)
        paid_amount = paid_amount.quantize(Decimal('0.001'))
        remaining = round(room.price - paid_amount, 2)

        print(remaining)

        deposit_paid = True
        request.data['paid_amount'] = paid_amount
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save(user=request.user, room=room, paid_amount=paid_amount, deposit_paid=deposit_paid)

        # Update the balance field of the booking object
        booking.balance = remaining
        booking.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
