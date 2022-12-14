from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Customer(models.Model):
    
    name = models.CharField(max_length=250)
    paternal_surname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class PaymentCustomer(models.Model):
    
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5000)])
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="payments")
    product_name = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    def __str__(self):
        return self.product_name