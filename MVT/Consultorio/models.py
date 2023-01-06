from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    affiliate_code = models.IntegerField(blank=False)
    diabetes = models.BooleanField(default=False)

class Orders(models.Model):
    order_type = models.CharField(blank=False)
    indication_date = models.DateField(blank=False)
    done = models.BooleanField(default=False)

class Medicines(models.model):
    name = models.CharField(blank=False)
    dose = models.FloatField(blank=False)
    indication_date = models.DateField(blank=False)
    diagnostic = models.CharField(max_length=100, blank=False)
    number = models.IntegerField(blank=False)


