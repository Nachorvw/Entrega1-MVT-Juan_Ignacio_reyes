from django.shortcuts import render
from Consultorio.models import Patient, Orders, Medicines
from Consultorio.forms import PatientsForm, OrdersForm, MedicinesForm
# Create your views here.

def patient_creation(request):
    #? funcion para poder crear pacientes ingresando la data por forms dentro del html

    if request.method == "GET": #? si recivimos un get, mostramos el formulario en create_patient.html
        context = {
            "form" : PatientsForm(),
        }
        return render (request, "patients/create_patient.html", context=context)


    elif request.method == "POST": #? si recivimos un post, creamos en este caso el paciente,con los datos que recivimos al completar el formularo en el get
        form = PatientsForm(request.POST)

        if form.is_valid(): #? si los datos son validos, se crea el paciente
            Patient.objects.create(
                name = form.cleaned_data["name"],
                surname = form.cleaned_data["surname"],
                age = form.cleaned_data["age"],
                dni = form.cleaned_data["dni"],
                birth_date = form.cleaned_data["birth_date"],
                affiliate_code = form.cleaned_data["affiliate_code"],
            )
            return render(request, "create_patient.html", context={})
        
        else: #? si los datos no son validos, se muestran los errores y devuelve el form para completarlo correctamente
            context = {
                "form_errors" : form.errors, #? para poder mostrar los errores en el html
                "form": PatientsForm(),
            }
            return render(request, "patients/create_patient.html", context=context)

def patient_list(request):
    #? funcion para listar la data de los pacientes en el html
    list_patient = Patient.objects.all
    context = {
        "patients" : list_patient,
    }
    return render(request, "patients/list_patients.html", context=context)

def order_creation(request):
    if request.method == "GET":
        context = {
            "form" : OrdersForm(),
        }
        return render(request, "orders/create_orders.html", context=context)

    elif request.method == "POST":
        form = OrdersForm(request.POST)

        if form.is_valid():
            Orders.objects.create(

                order_type = form.cleaned_data["order_type"],
                indication_date = form.cleaned_data["indication_date"],
                done = form.cleaned_data["done"],
                description = form.cleaned_data["description"],
            )
            return render(request, "orders/create_orders.html", context={})

        else:
            context = {
                "form_errors" : form.errors,
                "form" : OrdersForm(),
            }
            return render(request, "orders/create_orders.html", context=context)

def order_list(request):
    list_orders = Orders.objects.all
    context = {
        "order_list" : list_orders,
    }
    return render(request, "orders/list_orders.html", context=context)
    
def medicine_creation(request):
    pass

def medicine_list(request):
    pass