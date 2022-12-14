from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from webApp.models import Customer, PaymentCustomer
from webApp.api.serializers import CustomerSerializer, PaymentCustomerSerializer
from webApp.permissions import IsAdminOrReadOnly

class CustomersApiView(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True, context={'request': request})
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomersDetailApiView(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'Error': 'El cliente no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'Error': 'El cliente no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'Error': 'El cliente no existe'}, status=status.HTTP_404_NOT_FOUND)

        customer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

class PaymentsCustomersApiView(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        
        customers = PaymentCustomer.objects.all()
        serializer = PaymentCustomerSerializer(customers, many=True, context={'request': request})
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PaymentCustomerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaymentsCustomersDetailApiView(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            payment_customer = PaymentCustomer.objects.get(pk=pk)
        except PaymentCustomer.DoesNotExist:
            return Response({'Error': 'El pago no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentCustomerSerializer(payment_customer, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            payment_customer = PaymentCustomer.objects.get(pk=pk)
        except PaymentCustomer.DoesNotExist:
            return Response({'Error': 'El pago no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentCustomerSerializer(payment_customer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            payment_customer = PaymentCustomer.objects.get(pk=pk)
        except PaymentCustomer.DoesNotExist:
            return Response({'Error': 'El pago no existe'}, status=status.HTTP_404_NOT_FOUND)

        payment_customer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)