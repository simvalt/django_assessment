"""Users forms"""
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CustomUserCreationForm, CustomerCreationForm
from .models import Customer 
from django.contrib.messages.views import SuccessMessageMixin 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import for_admin, for_super_admin
#django rest
from rest_framework.response import Response
from rest_framework import generics
from .serlializers import CustomerSerializer, RegisterSerializer, CustomUserSerializer
from rest_framework.permissions import IsAuthenticated

#Admin login with template
class SignUpView(CreateView):
    """class sign up for custom signup"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

#Admin Registration custom django rest
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


#customer CRUD django rest framework
class CustomerListRest(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

@method_decorator([login_required, for_super_admin], name='dispatch')
class CustomerDetailRest(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


#customer CRUD without django rest(if we wants to use templates)

class CustomerList(ListView):
    """class to obtain customer list"""  
    model = Customer
    template_name = "customers/customer_list.html"

# @method_decorator([login_required, for_super_admin], name='dispatch')
# class CustomerCreate(SuccessMessageMixin, CreateView):
#     """class to create a customer""" 
#     model = Customer 
#     form_class = CustomerCreationForm
#     template_name = "customers/create_customer.html"
#     success_url = reverse_lazy("customerlist") 
#     success_message = 'Customer created successfully!' 

# class CustomerDetail(DetailView):
#     """class to obtain customer detail""" 
#     model = Customer 

# @method_decorator([login_required, for_super_admin], name='dispatch')
# class CustomerUpdate(SuccessMessageMixin, UpdateView): 
#     """class to update customer information"""
#     model = Customer 
#     form_class = CustomerCreationForm 
#     success_message = 'Customer updated successfully!' 

# @method_decorator([login_required, for_super_admin], name='dispatch')
# class CustomerDelete(SuccessMessageMixin, DeleteView): 
#     """class to delete customer"""
#     model = Customer 
#     form_class = CustomerCreationForm  

#     def get_success_url(self):       
#         return reverse_lazy('customerlist') 