from django.shortcuts import render

def quienes_somos(request):
    return render(request, "nosotros/quienes_somos.html")


def mision_vision(request):
    return render(request, "nosotros/mision_vision.html")


def estructura(request):
    return render(request, "nosotros/estructura.html")