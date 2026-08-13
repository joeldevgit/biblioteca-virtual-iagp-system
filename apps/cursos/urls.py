from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.index, name="index"),

    path("curso/<int:curso_id>/", views.curso_detalle, name="curso_detalle"),
]