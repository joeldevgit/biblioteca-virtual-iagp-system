from django.urls import path
from . import views

app_name = "biblioteca"

urlpatterns = [

    path(
        "",
        views.biblioteca,
        name="biblioteca"
    ),

    path(
        "jurisprudencia/<str:institucion>/",
        views.detalle_jurisprudencia,
        name="detalle_jurisprudencia"
    ),

]