from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers.supplier_serializer import SupplierSerializer

class SupplierRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

def index(request):
    return  HttpResponse("WELCOME TO THE WORLD")