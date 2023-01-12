"""MVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Consultorio.views import patient_creation, patient_list, order_creation, order_list, medicine_creation, medicine_list, MedicineUptade, PatientUpdate, OrderUpdate
from MVT.views import index
urlpatterns = [
    path("", index, name="index"),
    path('admin/', admin.site.urls),
    path("create-patient/", patient_creation),
    path("list-patients/", patient_list),
    path("update-patient/<int:pk>/", PatientUpdate.as_view()),
    path("create-order/", order_creation),
    path("list-orders/", order_list),
    path("update-order/<int:pk>/", OrderUpdate.as_view()),
    path("create-medicine/", medicine_creation),
    path("list-medicines/", medicine_list),
    path("update-medicine/<int:pk>/", MedicineUptade.as_view()),
]
