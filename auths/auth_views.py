from rest_framework.views import APIView
from rest_framework import generics
from auths.auths_model import *
from rest_framework.response import Response
from rest_framework import status
from serializers.supplier_serializer import SupplierSerializer
from serializers.customer_serializer import CustomerSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from custom_permissions.permissions import IsCustomer

class SupplierRegistrationView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)
    
class CustomerRegistrationView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = CustomerSerializer

class CustomerLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)