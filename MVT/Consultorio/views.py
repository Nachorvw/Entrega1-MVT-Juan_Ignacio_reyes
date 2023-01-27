from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Consultorio.models import Patient, Orders, Medicines
from Consultorio.forms import PatientsForm, OrdersForm, MedicinesForm
from users.models import UserProfile
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
            return render(request, "patients/create_patient.html", context={})
        
        else: #? si los datos no son validos, se muestran los errores y devuelve el form para completarlo correctamente
            context = {
                "form_errors" : form.errors, #? para poder mostrar los errores en el html
                "form": PatientsForm(),
            }
            return render(request, "patients/create_patient.html", context=context)

@login_required
def patient_list(request):

    #? funcion para listar la data de los pacientes en el html

    #? si el get nos trae un search (la barra de busqueda), filtramos los datos para mostrar los que contengan ese nombre
    if "search" in request.GET:
        search = request.GET["search"]
        list_patient = Patient.objects.filter(name__icontains = search)

    #? si no trae un search, mandamos toda la data normalmente
    else: 
        list_patient = Patient.objects.all()
    context = {
        "patients" : list_patient,
    }
    return render(request, "patients/list_patients.html", context=context)

def patientdetail(request,pk):
    #? funcion para ver con detalle el paciente
    patient_all = Patient.objects.get(id = pk)
    patient_orders = patient_all.orders_set.all()
    context = {
        "patient" : patient_all,
        "orders" : patient_orders,
    }
    return render(request, 'patients/patient_profile.html', context=context)

class PatientUpdate(UpdateView):
    #? funcion para actualizar los datos de un objeto en la base de datos (paciente)
    model = Patient
    fields = ["name", "surname", "age", "dni", "birth_date", "affiliate_code"]
    template_name= "patients/update_patient.html"
    success_url ="/list-patients/"

class PatientDelete(DeleteView):
    #? funcion para borrar un objeto de la base de datos (paciente)
    model = Patient
    template_name = 'patients/delete_patient.html'
    success_url = '/list-patients/'

def order_creation(request, pk):
    patient = Patient.objects.get(id = pk)
    form = OrdersForm(initial={"patient":patient})
    if request.method == "GET":
        
        context = {
            "form" : form,
            
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
                patient = form.cleaned_data["patient"]
                
            )
            return render(request, "orders/create_orders.html", context={})

        else:
            context = {
                "form_errors" : form.errors,
                "form" : OrdersForm(),
            }
            return render(request, "orders/create_orders.html", context=context)
@login_required
def order_list(request):
    
    if "search" in request.GET:
        search = request.GET["search"]
        list_orders = Orders.objects.filter(order_type__icontains = search)
    else:
        list_orders = Orders.objects.all()
    context = {
        "order_list": list_orders   
    }
    return render(request, "orders/list_orders.html", context=context)

class OrderUpdate(UpdateView):
    model = Orders
    fields = ["order_type", "indication_date", "done", "description"]
    template_name= "orders/update_order.html"
    success_url ="/list-orders/"

class OrderDelete(DeleteView):
    model = Orders
    template_name = 'Orders/delete_Order.html'
    success_url = '/list-orders/'

def medicine_creation(request):
    if request.method == "GET":
        context = {
            "form" : MedicinesForm(),
        }
        return render(request, "medicines/create_medicines.html", context=context)
    
    elif request.method == "POST":
        form = MedicinesForm(request.POST)

        if form.is_valid():
            Medicines.objects.create(
                name = form.cleaned_data["name"],
                dose = form.cleaned_data["dose"],
                indication_date = form.cleaned_data["indication_date"],
                diagnostic = form.cleaned_data["diagnostic"],
                number = form.cleaned_data["number"],
            )
            return render(request, "medicines/create_medicines.html")

        else:
            context = {
                "form_errors" : form.errors,
                "form" : MedicinesForm(),
            }
            return render(request, "medicines/create_medicines.html", context=context)
@login_required
def medicine_list(request):


    if "search" in request.GET:
        search = request.GET["search"]
        list_medicines = Medicines.objects.filter(name__icontains = search)
    else:
        list_medicines = Medicines.objects.all()
    context = {
        "medicine_list" : list_medicines,
    }
    return render(request, "medicines/list_medicines.html", context=context)

class MedicineUptade(UpdateView):

    model = Medicines
    fields = ["name", "dose", "indication_date", "diagnostic", "number"]
    template_name= "medicines/update_medicine.html"
    success_url ="/list-medicines/"

class MedicineDelete(DeleteView):
    model = Medicines
    template_name = 'medicines/delete_medicine.html'
    success_url = '/list-medicines/'