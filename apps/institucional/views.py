from django.shortcuts import render

def quienes_somos(request):
    return render(request, "institucional/quienes_somos.html")


def mision_vision(request):
    return render(request, "institucional/mision_vision.html")


def estructura(request):
    return render(request, "institucional/estructura.html")