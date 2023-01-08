from django.contrib import admin

# Register your models here.
from Consultorio.models import Patient, Medicines, Orders

admin.site.register(Patient)
admin.site.register(Medicines)
admin.site.register(Orders)