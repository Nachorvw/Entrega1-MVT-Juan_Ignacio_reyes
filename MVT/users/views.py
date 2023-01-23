from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, UserUpdateForm
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
            form.save()
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
