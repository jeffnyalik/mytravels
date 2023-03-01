from rest_framework import serializers
from api.models import *

class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Supplier
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'password']
    
    def validate(self, data):
        email = data.get('email')

        if Customer.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exist')
        return data
    

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Customer.objects.create_user(**validated_data, is_customer=True)
        user.set_password(password)
        user.save()
        return user




    
        
    

