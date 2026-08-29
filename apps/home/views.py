from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Testimonio


@login_required
def index(request):

    testimonios = Testimonio.objects.filter(
        activo=True
    ).order_by("orden")

    context = {
        "testimonios": testimonios,
    }

    return render(request, "home/home.html", context)
