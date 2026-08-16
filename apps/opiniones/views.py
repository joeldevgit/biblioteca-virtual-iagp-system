from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Opinion


def opiniones(request):

    opiniones_lista = Opinion.objects.all().order_by("-fecha")

    paginator = Paginator(opiniones_lista, 10)

    page_number = request.GET.get("page")

    opiniones = paginator.get_page(page_number)

    context = {
        "opiniones": opiniones,
    }

    return render(
        request,
        "opiniones/opiniones.html",
        context
    )