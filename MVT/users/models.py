from django.db import models
from Consultorio.models import Patient
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile")
    age = models.IntegerField(null = True, blank=True)
    dni = models.IntegerField(null = True, blank=True)
    birth_date = models.DateField(null = True, blank=True)
    affiliate_code = models.IntegerField(null = True, blank=True)
    phone = models.CharField(null = True, blank=True, max_length=100)
    profile_img = models.ImageField(upload_to="profile_images", null = True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'