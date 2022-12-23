from django.contrib import admin
from .models import Customers, Payments_customers, User

# Register your models here.
admin.site.register(Customers)
admin.site.register(Payments_customers)
admin.site.register(User)