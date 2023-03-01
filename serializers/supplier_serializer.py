from rest_framework import serializers
from api.models import *
from django.contrib.auth import authenticate

class SupplierSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Supplier
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'password']
    
    def validate(self, data):
        email = data.get('email')

        if Supplier.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exist')
        return data
    

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Supplier.objects.create_user(**validated_data, is_supplier=True)
        user.set_password(password)
        user.save()
        return user




    
        
    

