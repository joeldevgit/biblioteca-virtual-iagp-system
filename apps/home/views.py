from django.shortcuts import render

from .models import Testimonio
from apps.catalogo_academico.models import Curso


def index(request):

    testimonios = Testimonio.objects.filter(
        activo=True
    ).order_by("orden")

    cursos_vivo = Curso.objects.filter(
        activo=True,
        tipo="vivo"
    ).order_by("orden")

    cursos_virtual = Curso.objects.filter(
        activo=True,
        tipo="virtual"
    ).order_by("orden")

    context = {
        "testimonios": testimonios,
        "cursos_vivo": cursos_vivo,
        "cursos_virtual": cursos_virtual,
    }

    return render(request, "home/home.html", context)


def normatividad_directiva(request):
    return render(request, "home/normatividad_directiva.html")
