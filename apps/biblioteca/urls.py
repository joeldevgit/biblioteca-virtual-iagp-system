from django.urls import path

from . import views


app_name = "biblioteca"


urlpatterns = [
    path(
        "",
        views.biblioteca,
        name="biblioteca",
    ),

    path(
        "documentos/",
        views.listado_documentos,
        name="listado",
    ),

    path(
        "documento/<int:pk>/",
        views.detalle_documento,
        name="detalle",
    ),
]