from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="nombre")
    last_name = forms.CharField(max_length=100, required=True, label="apellido")
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label="nombre de usuario")
    first_name = forms.CharField(max_length=100, required=True, label="nombre")
    last_name = forms.CharField(max_length=100, required=True, label="apellido")
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
