from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import json
import base64

from webApp.core.login import post_admin, post_login
from webApp.forms import GenerateLoginForm, CustomerForm, PaymentsForm
from webApp.models import Administrators, Customers, Payments_Customers
from webApp.core.customers import create_customer, delete_customer, get_customer, get_customers, update_customer
from webApp.core.payments import create_payments, delete_payments, get_payments, update_payments


# Create your views here.


def login(request):
    form = GenerateLoginForm()
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': form,
        })
    else:
        form = GenerateLoginForm(request.POST or None)
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                return redirect('dashboard/'+str(user.id)+'/customers')
        return render(request, 'login.html', {
            'form': form,
        })


def customer_front(request, id):
    user = Administrators.objects.filter(id=id).first()
    customers = get_customers()
    customers_json = list(get_customers().values())
    customer_form = CustomerForm()
    if request.method == 'GET':
        return render(request, 'customers.html', {
            'user': user,
            'customers': customers,
            'customer_form': customer_form,
            'customers_json': customers_json
        })


def payments_front(request, id, customer):
    user = Administrators.objects.filter(id=id).first()
    payments = get_payments(customer)
    payments_json = list(payments.values())
    payment_form = PaymentsForm()
    if request.method == 'GET':
        return render(request, 'payments.html', {
            'user': user,
            'payments': payments,
            'payments_form': payment_form,
            'customer': customer,
            'payments_json': payments_json
        })


def customer_create(request, id):
    if request.method == 'POST':
        data = {
            "name": request.POST['name'],
            "paternal_surname": request.POST['paternal_surname'],
            "email": request.POST['email']
        }
        customer = create_customer(data)
        dummy_payments = {
            "amount": 200,
            "product_name": "Cheetos",
            "quantity": 10
        }
        create_payments(dummy_payments, customer.id)
        create_payments(dummy_payments, customer.id)
        return redirect('/dashboard/'+str(id)+'/customers')
    else:
        return redirect('/dashboard/'+str(id)+'/customers')


def customer_delete(request, id):
    if request.method == 'POST':
        delete_customer(request.POST['id'])
        return redirect('/dashboard/'+str(id)+'/customers')
    else:
        return redirect('/dashboard/'+str(id)+'/customers')


def customer_update(request, id):
    if request.method == 'POST':
        data = {
            "id": request.POST['id'],
            "name": request.POST['name'],
            "paternal_surname": request.POST['paternal_surname'],
            "email": request.POST['email']
        }
        update_customer(data)
        return redirect('/dashboard/'+str(id)+'/customers')
    else:
        return redirect('/dashboard/'+str(id)+'/customers')


def payments_create(request, id, customer):
    if request.method == 'POST':
        data = {
            "amount": request.POST['amount'],
            "product_name": request.POST['product_name'],
            "quantity": request.POST['quantity']
        }
        create_payments(data, customer)
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')
    else:
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')


def payments_delete(request, id, customer):
    if request.method == 'POST':
        delete_payments(request.POST['id'])
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')
    else:
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')


def payments_update(request, id, customer):
    if request.method == 'POST':
        data = {
            "id": request.POST['id'],
            "amount": request.POST['amount'],
            "product_name": request.POST['product_name'],
            "quantity": request.POST['quantity']
        }
        update_payments(data)
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')
    else:
        return redirect('/dashboard/'+str(id)+'/customers/'+str(customer)+'/payments')

@csrf_exempt
def api_login(request):
    data = {}
    if request.method == 'POST':
        try:
            post_body = json.loads(request.body.decode('utf-8'))
            login_data = {
                "name": post_body['name'],
                "password": post_body['password']
            }
            user = base64.b64encode(str(json.loads(post_login(login_data).toJSON())['id']).encode("ascii"))
            if user:
                data["message"] = "OK"
                data["token"] = user.decode("ascii")
                return JsonResponse(data, safe=False)

            else:
                data["message"] = "Error en el inicio de sesion"
                return JsonResponse(data, safe=False)
        except:
            data["message"] = 'Error en el inicio de sesion'
            return JsonResponse(data, safe=False)
    else:
        data["message"] = 'Error en el metodo para login, solo POST permitido'
        return JsonResponse(data, safe=False)

@csrf_exempt
def api_customers(request):
    try:
        token = base64.b64decode(str(request.META['HTTP_AUTHORIZATION']).split(' ')[1].encode("ascii"))
        user = post_admin(token.decode("ascii"))
    except:
        data["message"] = 'Error en header HTTP_AUTHORIZATION'
        return JsonResponse(data, safe=False)
    # Get Customers
    if request.method == 'GET':
        data = {}
        try:
            customers = list(get_customers().values())
            data["data"] = customers
            data["message"] = 'OK'
            return JsonResponse(data, safe=False)
        except:
            data["message"] = 'Error'
            return JsonResponse(data, safe=False)
    #Create Customers
    elif request.method == 'POST':
        data = {}
        if user.rol == 'super_administrator':
            try:
                post_body = json.loads(request.body.decode('utf-8'))
                create_data = {
                    "name": post_body['name'],
                    "paternal_surname": post_body['paternal_surname'],
                    "email": post_body['email']
                }
                customer = create_customer(create_data)
                data["data"] = json.loads(customer.toJSON())
                data["message"] = 'OK'
                return JsonResponse(data, safe=False)
            except:
                data["message"] = "Error para crear nuevo customer, falta uno o mas datos"
                return JsonResponse(data, safe=False)
        else:
            data["message"] = "No se tiene permisos de administrador para crear nuevos customers"
            return JsonResponse(data, safe=False)
    #Delete customers
    elif request.method == 'DELETE':
        data = {}
        if user.rol == 'super_administrator':
            try:
                post_body = json.loads(request.body.decode('utf-8'))
                customer = delete_customer(post_body['id'])
                data["data"] = json.loads(customer.toJSON())
                data["message"] = 'OK'
                return JsonResponse(data, safe=False)
            except:
                data["message"] = "Error para eliminar customer, falta uno o mas datos"
                return JsonResponse(data, safe=False)
        else:
            data["message"] = "No se tiene permisos de administrador para eliminar customers"
            return JsonResponse(data, safe=False)
    #Update customers
    elif request.method == 'PUT':
        data = {}
        if user.rol == 'super_administrator':
            try:
                post_body = json.loads(request.body.decode('utf-8'))
                data_update = {
                    "id": post_body['id'],
                    "name": post_body['name'],
                    "paternal_surname": post_body['paternal_surname'],
                    "email": post_body['email']
                }
                customer = update_customer(data_update)
                data["data"] = json.loads(customer.toJSON())
                data["message"] = 'OK'
                return JsonResponse(data, safe=False)
            except:
                data["message"] = "Error para actualizar customer, falta uno o mas datos"
                return JsonResponse(data, safe=False)
        else:
            data["message"] = "No se tiene permisos de administrador para actualizar customers"
            return JsonResponse(data, safe=False)

@csrf_exempt
def api_payments(request):
    try:
        token = base64.b64decode(str(request.META['HTTP_AUTHORIZATION']).split(' ')[1].encode("ascii"))
        user = post_admin(token.decode("ascii"))
    except:
        data["message"] = 'Error en header HTTP_AUTHORIZATION'
        return JsonResponse(data, safe=False)
    # Get Payments
    if request.method == 'GET':
        data = {}
        try:
            customer_id=request.GET.get('customer_id')
            payments = list(get_payments(customer_id).values())
            data["data"] = payments
            data["message"] = 'OK'
            return JsonResponse(data, safe=False)
        except:
            data["message"] = 'Error en la obtencion de pagos'
            return JsonResponse(data, safe=False)
    #Create Payments
    elif request.method == 'POST':
        data = {}
        if user.rol == 'super_administrator':
            try:
                post_body = json.loads(request.body.decode('utf-8'))
                create_data = {
                    "amount": post_body['amount'],
                    "product_name": post_body['product_name'],
                    "quantity": post_body['quantity'],
                }
                customer = create_payments(create_data,post_body["customer_id"])
                data["data"] = json.loads(customer.toJSON())
                data["message"] = 'OK'
                return JsonResponse(data, safe=False)
            except:
                data["message"] = "Error para insertar nuevo payment, falta uno o mas datos"
                return JsonResponse(data, safe=False)
        else:
            data["message"] = "No se tiene permisos de administrador para insertar nuevos payments"
            return JsonResponse(data, safe=False)
    #Delete Payments
    elif request.method == 'DELETE':
        data = {}
        if user.rol == 'super_administrator':
            try:
                post_body = json.loads(request.body.decode('utf-8'))
                payment = delete_payments(post_body['id'])
                data["data"] = json.loads(payment.toJSON())
                data["message"] = 'OK'
                return JsonResponse(data, safe=False)
            except:
                data["message"] = "Error para eliminar payment, falta uno o mas datos"
                return JsonResponse(data, safe=False)
        else:
            data["message"] = "No se tiene permisos de administrador para eliminar payments"
            return JsonResponse(data, safe=False)
    #Update Payments
    elif request.method == 'PUT':
        data = {}
        if user.rol == 'super_administrator':
            try:
                post_body = json.loads(request.body.decode('utf-8'))
                data_update = {
                    "id": post_body['id'],
                    "amount": post_body['amount'],
                    "product_name": post_body['product_name'],
                    "quantity": post_body['quantity']
                }
                payment = update_payments(data_update)
                data["data"] = json.loads(payment.toJSON())
                data["message"] = 'OK'
                return JsonResponse(data, safe=False)
            except:
                data["message"] = "Error para actualizar payment, falta uno o mas datos"
                return JsonResponse(data, safe=False)
        else:
            data["message"] = "No se tiene permisos de administrador para actualizar payments"
            return JsonResponse(data, safe=False)