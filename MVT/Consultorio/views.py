from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from Consultorio.models import Patient, Orders, Medicines
from Consultorio.forms import PatientsForm, OrdersForm, MedicinesForm
from MVT.decorators import allowed_users
# Create your views here.
@allowed_users(allowed_roles=["Admin"])
def patient_creation(request):
    #? function to create patients from the html

    if request.method == "GET": #?if we receive a get, we show the form
        context = {
            "form" : PatientsForm(),
        }
        return render (request, "patients/create_patient.html", context=context)


    elif request.method == "POST": #?if we receive a post, we atempt to create the patient with the data from the form
        form = PatientsForm(request.POST)

        if form.is_valid(): #?if the data is valid, we create the patient
            Patient.objects.create(
                name = form.cleaned_data["name"],
                surname = form.cleaned_data["surname"],
                age = form.cleaned_data["age"],
                dni = form.cleaned_data["dni"],
                birth_date = form.cleaned_data["birth_date"],
                affiliate_code = form.cleaned_data["affiliate_code"],
            )
            return render(request, "patients/create_patient.html", context={})
        
        else: #?if the data is not valid, we show the errors and return the form again
            context = {
                "form_errors" : form.errors,
                "form": PatientsForm(),
            }
            return render(request, "patients/create_patient.html", context=context)

@login_required
def patient_list(request):

    #? function for listing the patients in the html

    #? if we receive a "search" from GET, we filter the data
    if "search" in request.GET:
        search = request.GET["search"]
        list_patient = Patient.objects.filter(name__icontains = search)

    #? if not, we send all the data
    else: 
        list_patient = Patient.objects.all()
    context = {
        "patients" : list_patient,
    }
    return render(request, "patients/list_patients.html", context=context)

@allowed_users(allowed_roles=["Admin"])
def patientdetail(request,pk):
    #? function for patient profile
    patient_all = Patient.objects.get(id = pk)
    patient_orders = patient_all.orders_set.all()
    context = {
        "patient" : patient_all,
        "orders" : patient_orders,
    }
    return render(request, 'patients/patient_profile.html', context=context)

class PatientUpdate(PermissionRequiredMixin,UpdateView):
    #? function to update the data in the db (patient)
    permission_required = "patient.change_patient" #?we search for the permission in the user, if he has one, we let him enter the view, if not we send an error
    model = Patient
    fields = ["name", "surname", "age", "dni", "birth_date", "affiliate_code"]
    template_name= "patients/update_patient.html"
    success_url ="/list-patients/"

class PatientDelete(PermissionRequiredMixin,DeleteView):
    #? function to delete an object from the db (patient)
    permission_required = "patient.delete_patient" #? we search for the permission in the user, if he has one, we let him enter the view, if not we send an error
    model = Patient
    template_name = 'patients/delete_patient.html'
    success_url = '/list-patients/'

@allowed_users(allowed_roles=["Admin"])
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

class OrderUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "order.change_order"
    model = Orders
    fields = ["order_type", "indication_date", "done", "description"]
    template_name= "orders/update_order.html"
    success_url ="/list-orders/"

class OrderDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "order.delete_order"
    model = Orders
    template_name = 'Orders/delete_Order.html'
    success_url = '/list-orders/'

@allowed_users(allowed_roles=["Admin"])
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

class MedicineUptade(PermissionRequiredMixin, UpdateView):
    permission_required = "medicine.change_medicine"
    model = Medicines
    fields = ["name", "dose", "indication_date", "diagnostic", "number"]
    template_name= "medicines/update_medicine.html"
    success_url ="/list-medicines/"

class MedicineDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "medicine.delete_medicine"
    model = Medicines
    template_name = 'medicines/delete_medicine.html'
    success_url = '/list-medicines/'