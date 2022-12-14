"""serializers for payments app"""
from django.db.models import fields
from rest_framework import serializers
from .models import PaymentsCustomers
  
class PaymentsCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsCustomers
        fields = ('customer_id', 'name', 'paternal_surname', 'email')