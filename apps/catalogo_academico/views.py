from django.shortcuts import render
from .models import Curso

def index(request):

    cursos_vivo = Curso.objects.filter(
        tipo="vivo",
        activo=True
    ).order_by("orden")

    cursos_virtual = Curso.objects.filter(
        tipo="virtual",
        activo=True
    ).order_by("orden")

    return render(request, "catalogo_academico/index.html", {
        "cursos_vivo": cursos_vivo,
        "cursos_virtual": cursos_virtual,
    })



