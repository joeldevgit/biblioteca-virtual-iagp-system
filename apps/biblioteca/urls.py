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

    path(
        "documento/<int:pk>/descargar/",
        views.documento_descargar,
        name="descargar",
    ),

    path(
        "gestion/documentos/",
        views.gestion_documentos,
        name="gestion_documentos",
    ),

    path(
        "gestion/documentos/crear/",
        views.documento_crear,
        name="documento_crear",
    ),

    path(
        "gestion/documentos/<int:pk>/editar/",
        views.documento_editar,
        name="documento_editar",
    ),

    path(
        "gestion/documentos/<int:pk>/estado/",
        views.documento_estado,
        name="documento_estado",
    ),
]