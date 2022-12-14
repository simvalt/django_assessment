"""views for payment app"""
from django.shortcuts import render
from .models import PaymentsCustomers
from rest_framework import generics
from .serializers import PaymentsCustomersSerializer
from rest_framework.permissions import IsAuthenticated

#crud payments
class PaymentsCustomerListRest(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PaymentsCustomers.objects.all()
    serializer_class = PaymentsCustomersSerializer


class PaymentsCustomerDetailRest(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PaymentsCustomers.objects.all()
    serializer_class = PaymentsCustomersSerializer
