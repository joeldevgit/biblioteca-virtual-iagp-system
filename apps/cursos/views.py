from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
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

    return render(request, "cursos/index.html", {
        "cursos_vivo": cursos_vivo,
        "cursos_virtual": cursos_virtual,
    })


def curso_detalle(request, curso_id):

    curso = get_object_or_404(
        Curso,
        id=curso_id
    )

    return render(
        request,
        "cursos/curso-detalle.html",
        {
            "curso": curso
        }
    )