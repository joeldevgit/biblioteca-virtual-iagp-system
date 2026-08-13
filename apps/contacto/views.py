from django.shortcuts import render, redirect
from .models import Contacto

def index(request):

    if request.method == "POST":

        Contacto.objects.create(
            nombre=request.POST["nombre"],
            email=request.POST["email"],
            departamento=request.POST["departamento"],
            compania=request.POST["compania"],
            movil=request.POST["movil"],
            mensaje=request.POST["mensaje"],
        )

        return redirect("contacto:index")

    return render(request, "contacto/index.html")