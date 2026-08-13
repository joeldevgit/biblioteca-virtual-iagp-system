from django.shortcuts import render
from .models import Opinion


def opiniones(request):

    opiniones = Opinion.objects.all()

    context = {
        "opiniones": opiniones,
    }

    return render(
        request,
        "opiniones/opiniones.html",
        context
    )