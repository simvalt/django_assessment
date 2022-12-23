from django import forms
from models import *

class UsersForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'password']
        widgets = {
            'password': forms.PasswordInput()
        }