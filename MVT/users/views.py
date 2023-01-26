from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, UserUpdateForm, UserProfileForm
from users.models import UserProfile
from Consultorio.models import Patient
# Create your views here.

def user_login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "users/login.html", context=context)

    elif request.method == "POST":
        form = AuthenticationForm(request = request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {
                    "message" : f"bienvenido {username}!"
                }
                return render(request, "index.html", context=context)

        form = AuthenticationForm()
        context = {
            "form": form,
            "errors": "credenciales incorrectas",
        }
        return render(request, "users/login.html", context=context)
        

def user_register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "users/register.html", context=context)

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, affiliate_code = form.cleaned_data["affiliate_code"])
            return redirect("login")
        context = {
            "errors": form.errors,
            "form": RegisterForm(),
        }
        return render(request, "users/register.html", context=context)

@login_required
def update_user(request):

    user = request.user
    if request.method == "GET":
        form = UserUpdateForm(
            initial = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,

            } 
        )
        context = {
            "form": form
        }
        return render(request, "users/update_user.html", context=context)

    elif request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get("username")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect("index")
        context = {
            "errors": form.errors,
            "form": UserUpdateForm(),
        }
        return render(request, "users/update_user.html", context=context)

def user_profile(request):
    pass

def update_user_profile(request):
    if request.method == "GET":
        form = UserProfileForm(initial={
            "age" : request.user.profile.age,
            "dni" : request.user.profile.dni,
            "birth_date" :request.user.profile.birth_date,
            "phone" : request.user.profile.phone,
            "profile_img" : request.user.profile.profile_img,
        })
        context = {
            "form": form
        }
        return render(request, "users/update_profile.html", context=context)

    elif request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():

            user.profile.age = form.cleaned_data.get("age")
            user.profile.dni = form.cleaned_data.get("dni")
            user.profile.birth_date = form.cleaned_data.get("birth_date")
            user.profile.phone = form.cleaned_data.get("phone")
            user.profile.profile_img = form.cleaned_data.get("profile_img")
            user.profile.save()
            return redirect("index")
        context = {
            "errors": form.errors,
            "form": UserProfileForm(),
        }
        return render(request, "users/register.html", context=context)
