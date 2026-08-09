from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),

    path("articulo-detalle/", views.articulo_detalle, name="articulo_detalle"),
    path("noticia-detalle/", views.noticia_detalle, name="noticia_detalle"),
    path("norma-detalle/", views.norma_detalle, name="norma_detalle"),
]