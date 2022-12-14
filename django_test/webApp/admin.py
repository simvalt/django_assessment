from django.contrib import admin
from webApp.models import Customer, PaymentCustomer

# Register your models here.

admin.site.register(Customer)
admin.site.register(PaymentCustomer)