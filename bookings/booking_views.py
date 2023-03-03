from serializers.booking_serializer import *
from bookings.booking_model import *
from rest_framework import generics
from custom_permissions.permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class BookingApiView(generics.CreateAPIView):
    serializer_class = BookingSerizer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        user = self.request.user
        if user.IsCustomer:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def pay_deposit(self, request, pk=None):
        booking = self.get_object()
        booking.deposit_paid = True
        booking.paid_amount = booking.room.price * 0.2
        booking.save()
        return Response({'status': 'deposit paid'})
    
    @action(detail=True, methods=['post'])
    def pay_remaining(self, request, pk=None):
        booking = self.get_object()
        if booking.deposit_paid:
            booking.paid_amount = booking.room.price - (booking.room.price * 0.2)
            booking.save()
            return Response({'status': 'remaining amount paid'})
        else:
            return Response({'status': 'deposit not paid'})
