from django.shortcuts import render

def index(request):
    return render(request, "catalogo_academico/index.html")