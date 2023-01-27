from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserProfile
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="nombre")
    last_name = forms.CharField(max_length=100, required=True, label="apellido")
    affiliate_code = forms.IntegerField(required=True, label="numero de afiliado")
    dni = forms.IntegerField(required=True, label="dni")
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

class UserProfileForm(forms.ModelForm):
    
    class Meta:
            model = UserProfile
            fields = ["age", "dni", "birth_date", "phone", "profile_img"]