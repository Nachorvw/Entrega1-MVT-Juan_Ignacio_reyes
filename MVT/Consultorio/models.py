from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    dni = models.IntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    affiliate_code = models.IntegerField(blank=False)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        

class Orders(models.Model):
    order_choices = (
        ("Laboratorio", "Laboratorio"),
        ("Consulta con profesional", "Consulta con profesional"),
        ("Estudios", "Estudios"), 
        ("Otros", "Otros"),
    )
    order_type = models.CharField(choices=order_choices, max_length=100)
    indication_date = models.DateField(blank=False)
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
    
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.order_type

class Medicines(models.Model):
    name = models.CharField(max_length=50,blank=False)
    dose = models.FloatField(blank=False)
    indication_date = models.DateField(blank=False)
    diagnostic = models.CharField(max_length=100, blank=False)
    number = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        

