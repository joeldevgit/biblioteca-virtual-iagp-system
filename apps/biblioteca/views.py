from django.shortcuts import render, get_object_or_404

from .models import Institucion, Jurisprudencia


def biblioteca(request):

    instituciones = Institucion.objects.filter(
        activo=True
    )

    return render(
        request,
        "biblioteca/biblioteca.html",
        {
            "instituciones": instituciones,
        }
    )



def detalle_jurisprudencia(request, institucion):

    institucion_obj = get_object_or_404(
        Institucion,
        slug=institucion,
        activo=True
    )

    instituciones = Institucion.objects.filter(
        activo=True
    )

    tipo = request.GET.get("tipo", "opinion")

    jurisprudencias = Jurisprudencia.objects.filter(
        institucion=institucion_obj,
        activo=True,
        tipo=tipo
    ).order_by(
        "-año",
        "-fecha",
        "-created_at"
    )

    temas = (
        jurisprudencias
        .exclude(tema="")
        .values_list(
            "tema",
            flat=True
        )
        .distinct()
    )

    return render(
        request,
        "biblioteca/detalle-jurisprudencia.html",
        {
            "institucion": institucion_obj,
            "instituciones": instituciones,
            "jurisprudencias": jurisprudencias,
            "temas": temas,
            "tipo": tipo,
        }
    )