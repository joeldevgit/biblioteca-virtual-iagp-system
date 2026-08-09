from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html")

def articulo_detalle(request):
    return render(request, "blog/articulo-detalle.html")

def noticia_detalle(request):
    return render(request, "blog/noticia-detalle.html")

def norma_detalle(request):
    return render(request, "blog/norma-detalle.html")