from django.shortcuts import render
from Consultorio.models import Media

def index(request):
    media = Media.objects.first()
    context = {
        "media" : media
    }
    return render(request, "index.html", context=context)

def about_us(request):
    
    return render(request, "about_us.html", context={})