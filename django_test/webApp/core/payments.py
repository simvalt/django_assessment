from webApp.models import Customers, Payments_Customers


def get_payments(id):
    return Payments_Customers.objects.filter(customer_id=id)


def get_payment(id):
    return Payments_Customers.objects.filter(id=id).first()


def create_payments(data,c_id):
    payments = Payments_Customers.objects.create(
        amount=data['amount'],
        customer_id=Customers.objects.filter(id=c_id).first(),
        product_name=data['product_name'],
        quantity=data['quantity']
    )
    return payments

def update_payments(data):
    payments = get_payment(data['id'])
    payments.amount = data['amount']
    payments.product_name = data['product_name']
    payments.quantity = data['quantity']
    payments.save()
    return payments

def delete_payments(id):
    payments = get_payment(id)
    payments.delete()
    return payments
