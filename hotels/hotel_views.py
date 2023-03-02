from rest_framework import generics
from hotels.hotel_model import *
from serializers.hotel_serializer import *
from rest_framework.permissions import IsAuthenticated
from custom_permissions.permissions import IsSupplier, IsCustomer

class HotelView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,IsSupplier]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

