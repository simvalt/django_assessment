from django.db import models

ROLES = [
    ('admin', 'administrator'), 
    ('super', 'super_administrator'),]

# Create your models here.
class Customers(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=50, blank=False)
    paternal_surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Payments_customers(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    amount = models.FloatField(blank=True, null=True)
    customer_id = models.ForeignKey("webApp.Customers", blank=False, null=False, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50)
    rol = models.CharField(max_length=15, choices=ROLES, default='admin')

    def __str__(self):
        return self.name