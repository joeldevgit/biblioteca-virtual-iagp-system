from django.shortcuts import render


def opiniones(request):
    return render(request, "opiniones_osce/opiniones.html")