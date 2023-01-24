from django.contrib import admin
from users.models import UserProfile
# Register your models here.
@admin.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","age", "dni", "birth_date", "affiliate_code", "phone", "profile_img")
    
