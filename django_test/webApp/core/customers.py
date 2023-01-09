from webApp.models import Customers


def get_customers():
    return Customers.objects.all()


def get_customer(id):
    return Customers.objects.filter(id=id).first()


def create_customer(data):
    customer = Customers.objects.create(
        name=data['name'],
        paternal_surname=data['paternal_surname'],
        email=data['email']
    )
    return customer

def update_customer(data):
    customer = Customers.objects.get(id=data['id'])
    customer.email = data['email']
    customer.name = data['name']
    customer.paternal_surname = data['paternal_surname']
    customer.save()
    return customer

def delete_customer(id):
    customer = get_customer(id)
    customer.delete()
    return customer
