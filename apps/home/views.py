from django.shortcuts import render

from .models import Testimonio



def index(request):

    testimonios = Testimonio.objects.filter(
        activo=True
    ).order_by("orden")



    context = {
        "testimonios": testimonios,
    }
 
    return render(request, 'home/home.html', context)


def normatividad_directiva(request):
    return render(request, "home/normatividad_directiva.html")
