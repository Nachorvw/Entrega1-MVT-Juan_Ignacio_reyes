from django import forms
from Consultorio.models import Patient


class PatientsForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    age = forms.IntegerField()
    dni = forms.IntegerField()
    birth_date = forms.DateField()
    affiliate_code = forms.IntegerField()

class OrdersForm(forms.Form):
    order_choices = (
        ("Laboratorio", "Laboratorio"),
        ("Consulta con profesional", "Consulta con profesional"),
        ("Estudios", "Estudios"),
        ("Otros", "Otros"),
    )
    order_type = forms.ChoiceField(choices=order_choices)
    indication_date = forms.DateField()
    done = forms.BooleanField(required=False)
    description = forms.CharField(max_length=200)
    patient = Patient.objects.all()
class MedicinesForm(forms.Form):
    name = forms.CharField(max_length=50)
    dose = forms.FloatField()
    indication_date = forms.DateField()
    diagnostic = forms.CharField(max_length=100)
    number = forms.IntegerField()