from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, UserUpdateForm, UserProfileForm
from users.models import UserProfile
from MVT.decorators import logged_in_user, allowed_users


@logged_in_user
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
                return redirect("index")

        form = AuthenticationForm()
        context = {
            "form": form,
            "errors": "credenciales incorrectas",
        }
        return render(request, "users/login.html", context=context)
        
@logged_in_user
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
            UserProfile.objects.create(user=user, affiliate_code = form.cleaned_data["affiliate_code"], dni = form.cleaned_data["dni"])
            group = Group.objects.get(name = ("Paciente")) #?when we create a patient, it gets assigned the "paciente" group
            user.groups.add(group)
            return redirect("login")
        context = {
            "errors": form.errors,
            "form": RegisterForm(),
        }
        return render(request, "users/register.html", context=context)

@login_required
@allowed_users(allowed_roles=["Paciente"])
def update_user(request):

    user = request.user
    if request.method == "GET":
        form = UserUpdateForm(#? we get the data from the object 
            initial = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            } 
        )
        context = {
            "form_user": form
        }
        return render(request, "users/update_profile.html", context=context)

    elif request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get("username")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect("/user-profile/") #? if all is valid, we redirect the user to its profile with the updated data
        context = {
            "errors": form.errors,
            "form": UserUpdateForm(),
        }
        return render(request, "users/update_profile.html", context=context)

@login_required
def user_profile_page(request):
    #? a "fix" to the (RelatedObjectDoesNotExist) we try to get the patient in the user
    try:
        orders = request.user.patient.orders_set.all() #? we get the orders from the patient in that user
        context = {
        "orders" : orders,
        }
    except: #? if the user has no patient, we simply return nothing
        context = {
        }
    return render(request, "users/user_profile.html", context=context)

@login_required
@allowed_users(allowed_roles=["Paciente"])
def update_user_profile(request):
    if request.method == "GET":
        user = request.user
        form = UserProfileForm(initial={
            "age" : user.profile.age,
            "dni" : user.profile.dni,
            "phone" : user.profile.phone,
            "profile_img" : user.profile.profile_img,
        })
        context = {
            "form_profile": form,
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
            return redirect("/user-profile/")
        context = {
            "errors": form.errors,
            "form": UserProfileForm(),
        }
        return render(request, "users/register.html", context=context)
