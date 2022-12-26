from django.shortcuts import render, redirect
from .models import Customers

# Create your views here.
def home(request):
    customers = Customers.objects.all()
    return render(request, "customers.html", {"customers": customers})

def registrarCustomers(request):
    id = request.POST['txtid']
    name = request.POST['txtNombre']
    paternal_surname = request.POST['txtApellido']
    email = request.POST['txtEmail']

    customer=Customers.objects.create(id=id, name=name, paternal_surname=paternal_surname, email=email)

    return redirect('/')

def editarCustomer(request, id):
    customer = Customers.objects.get(id=id)
    return render(request, "editarCustomer.html", {"customer": customer})

def editarCustomers(request):
    id = request.POST['txtid']
    name = request.POST['txtNombre']
    paternal_surname = request.POST['txtApellido']
    email = request.POST['txtEmail']

    customer = Customers.objects.get(id=id)
    customer.name = name
    customer.paternal_surname = paternal_surname
    customer.email = email
    customer.save()

    return redirect('/')

def eliminarCustomer(request, id):
    Customer = Customers.objects.get(id=id)
    Customer.delete()

    return redirect('/')
