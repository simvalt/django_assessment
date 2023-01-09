from django.shortcuts import render, redirect
from django.core import serializers

from webApp.forms import GenerateLoginForm, CustomerForm, PaymentsForm
from webApp.models import Administrators, Customers, Payments_Customers
from webApp.core.customers import create_customer, delete_customer,get_customers, update_customer
from webApp.core.payments import create_payments, delete_payments, get_payments, update_payments
import json

# Create your views here.
def login(request):
    form = GenerateLoginForm()
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form':form,
        })
    else:
        form = GenerateLoginForm(request.POST or None)
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                return redirect('dashboard/'+str(user.id)+'/customers')
        return render(request, 'login.html', {
                'form':form,
        })

def customer_front(request,id):
    user = Administrators.objects.filter(id=id).first()
    customers = get_customers()
    customers_json = list(get_customers().values())
    customer_form = CustomerForm()
    if request.method == 'GET':
        return render(request, 'customers.html', {
            'user':user,
            'customers':customers,
            'customer_form':customer_form,
            'customers_json':customers_json
    })

def payments_front(request,id,customer):
    user = Administrators.objects.filter(id=id).first()
    payments = get_payments(customer)
    payments_json = list(payments.values())
    payment_form = PaymentsForm()
    if request.method == 'GET':
        return render(request, 'payments.html', {
            'user':user,
            'payments':payments,
            'payments_form':payment_form,
            'customer':customer,
            'payments_json':payments_json
    })
    
def customer_create(request,id):
    if request.method == 'POST':
        data = {
            "name":request.POST['name'],
            "paternal_surname":request.POST['paternal_surname'],
            "email":request.POST['email']
        }
        customer = create_customer(data)
        dummy_payments = {
            "amount":200,
            "product_name":"Cheetos",
            "quantity":10
        }
        create_payments(dummy_payments,customer.id)
        create_payments(dummy_payments,customer.id)
        return redirect('/dashboard/'+str(id)+'/customers')
    else:
        return redirect('/dashboard/'+str(id)+'/customers')

def customer_delete(request,id):
    if request.method == 'POST':
        delete_customer(request.POST['id'])
        return redirect('/dashboard/'+str(id)+'/customers')
    else:
        return redirect('/dashboard/'+str(id)+'/customers')

def customer_update(request,id):
    if request.method == 'POST':
        data = {
            "id":request.POST['id'],
            "name":request.POST['name'],
            "paternal_surname":request.POST['paternal_surname'],
            "email":request.POST['email']
        }
        update_customer(data)
        return redirect('/dashboard/'+str(id)+'/customers')
    else:
        return redirect('/dashboard/'+str(id)+'/customers')

def payments_create(request,id,customer):
    if request.method == 'POST':
        data = {
            "amount":request.POST['amount'],
            "product_name":request.POST['product_name'],
            "quantity":request.POST['quantity']
        }
        create_payments(data,customer)
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')
    else:
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')

def payments_delete(request,id,customer):
    if request.method == 'POST':
        delete_payments(request.POST['id'])
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')
    else:
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')

def payments_update(request,id,customer):
    if request.method == 'POST':
        data = {
            "id":request.POST['id'],
            "amount":request.POST['amount'],
            "product_name":request.POST['product_name'],
            "quantity":request.POST['quantity']
        }
        update_payments(data)
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')
    else:
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')