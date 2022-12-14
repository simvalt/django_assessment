"""Forms for user app"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Customer


#forms for users
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username","base_role")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username","base_role")

#forms for customers
class CustomerCreationForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__" 

