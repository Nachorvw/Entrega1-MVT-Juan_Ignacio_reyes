from django import forms
from django.forms import ModelForm
from Consultorio.models import Orders


class PatientsForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    age = forms.IntegerField()
    dni = forms.IntegerField()
    birth_date = forms.DateField()
    affiliate_code = forms.IntegerField()

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"


class MedicinesForm(forms.Form):
    name = forms.CharField(max_length=50)
    dose = forms.FloatField()
    indication_date = forms.DateField()
    diagnostic = forms.CharField(max_length=100)
    number = forms.IntegerField()