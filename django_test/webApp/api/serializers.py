from rest_framework import serializers
from webApp.models import Customer, PaymentCustomer

class PaymentCustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PaymentCustomer
        fields = "__all__"
        
class CustomerSerializer(serializers.ModelSerializer):
    
    payments = PaymentCustomerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = "__all__"