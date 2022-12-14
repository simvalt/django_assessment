from django.db.models import fields
from rest_framework import serializers
from .models import Customer, CustomUser
  
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'name', 'paternal_surname', 'email')

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username","base_role")
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user

# User serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username","base_role")