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
