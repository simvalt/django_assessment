"""Models for user app"""
from django.db import models
from django.contrib.auth.models  import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """Custom model for users"""
    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", 'Super_Admin'
        ADMIN = "ADMIN", 'Admin'    
    admin_id = models.AutoField(primary_key=True,verbose_name=_("id customer"))
    base_role = models.CharField(max_length=50,choices=Role.choices,verbose_name=_("Admin role") )

    def __str__(self):
        return self.username


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True,verbose_name=_("id customer"))
    name = models.CharField(max_length=100,verbose_name=_("Customer name"))
    paternal_surname = models.CharField(max_length=100,verbose_name=_("Customer paternal surname"))
    email = models.EmailField(max_length=200,verbose_name=_("Customer email"))

    def __str__(self):
        return self.name