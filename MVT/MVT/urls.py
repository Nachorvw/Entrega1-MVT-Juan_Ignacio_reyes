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
from Consultorio.views import patient_creation, patient_list, order_creation, order_list, medicine_creation, medicine_list, MedicineUptade, PatientUpdate, OrderUpdate, MedicineDelete, PatientDelete, OrderDelete, patientdetail
from MVT.views import index, about_us
from users.views import user_login, user_register, update_user, update_user_profile, user_profile_page
from django.contrib.auth.views import LogoutView
from MVT.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
urlpatterns = [
    path("", index, name="index"),
    path('admin/', admin.site.urls,),
    path("about-us/", about_us, name="about-us"),
    #---patients---
    path("create-patient/", patient_creation, name="patient-create"),
    path("list-patients/", patient_list, name="patient-list"),
    path("update-patient/<int:pk>/", PatientUpdate.as_view(), name="patient-update"),
    path("delete-patient/<int:pk>/", PatientDelete.as_view(), name="patient-delete"),
    path('profile/<int:pk>/', patientdetail, name="patient-profile"),
    #---orders---
    path("create-order/<int:pk>/", order_creation, name="order-create"),
    path("list-orders/", order_list, name="order-list"),
    path("update-order/<int:pk>/", OrderUpdate.as_view(), name="order-update"),
    path("delete-order/<int:pk>/", OrderDelete.as_view(), name="order-delete"),
    #---medicines---
    path("create-medicine/", medicine_creation, name="medicine-create"),
    path("list-medicines/", medicine_list, name="medicine-list"),
    path("update-medicine/<int:pk>/", MedicineUptade.as_view(), name="medicine-update"),
    path("delete-medicine/<int:pk>/", MedicineDelete.as_view(), name="medicine-delete"),
    #---user---
    path("login/", user_login, name="login"),
    path("logout/", LogoutView.as_view(template_name = "users/logout.html")),
    path("register/", user_register, name="register"),
    path("update-user/", update_user, name="user-update"),
    path("update-profile/", update_user_profile, name="profile-update"),
    path("user-profile/", user_profile_page, name="user-profile")

] + static(MEDIA_URL, document_root = MEDIA_ROOT)
