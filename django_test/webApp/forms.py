from django import forms

from webApp.models import Administrators

class GenerateLoginForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'input-field','placeholder':'Nombre'}))
    password=forms.CharField( max_length=200,widget=forms.PasswordInput(render_value=False, attrs={'class': 'input-field','placeholder':'Contraseña'}))

    def clean(self):
        username = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        user = Administrators.objects.filter(name=username).filter(password=password)
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self,request):
        name = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        user = Administrators.objects.filter(name=name).filter(password=password).first()
        return user

class CustomerForm(forms.Form):
    id= forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'ID','disabled':True}))
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa el nombre'}))
    paternal_surname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa el apellido'}))
    email = forms.CharField(max_length=200, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Ingresa Email'}))

class PaymentsForm(forms.Form):
    id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'ID','disabled':True}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingresa el monto'}))
    product_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa el nombre del producto'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingresa la cantidad de productos'}))