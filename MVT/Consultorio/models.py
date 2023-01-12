from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    dni = models.IntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    affiliate_code = models.IntegerField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

class Orders(models.Model):
    order_type = models.CharField(max_length=50,blank=False)
    indication_date = models.DateField(blank=False)
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.order_type

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

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

