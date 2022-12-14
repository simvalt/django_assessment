"""Models for payments app"""
from django.db import models
from user.models import Customer
from django.utils.translation import gettext_lazy as _

class PaymentsCustomers(models.Model):
    id_payment = models.AutoField(primary_key=True,verbose_name=_("id customer"))
    amount = models.CharField(max_length=100, null=True,verbose_name=_("Amount of products"))
    customer_id =models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name=_("id customer"))
    product_name = models.CharField(max_length=100, null=True,verbose_name=_("Product Name"))
    quantity = models.IntegerField(verbose_name=_("Quiantity"))

    def __str__(self):
        return self.product_name    
