import json
from django.db import models

class Customers(models.Model):

    name = models.CharField(max_length=200)
    paternal_surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name+" "+self.paternal_surname

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Payments_Customers(models.Model):
    amount = models.IntegerField()
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Administrators(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    rol = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
