from django.contrib import admin

from .models import (
    Categoria,
    Institucion,
    TipoDocumento,
    Documento,
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "slug",
        "activo",
    )

    list_filter = (
        "activo",
    )

    search_fields = (
        "nombre",
        "descripcion",
    )

    prepopulated_fields = {
        "slug": ("nombre",)
    }


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "sigla",
        "activo",
    )

    list_filter = (
        "activo",
    )

    search_fields = (
        "nombre",
        "sigla",
    )


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "categoria",
        "activo",
    )

    list_filter = (
        "categoria",
        "activo",
    )

    search_fields = (
        "nombre",
        "descripcion",
    )


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "institucion",
        "tipo",
        "anio",
        "fecha",
        "activo",
    )

    list_filter = (
        "categoria",
        "institucion",
        "tipo",
        "anio",
        "activo",
    )

    search_fields = (
        "titulo",
        "tema",
        "descripcion",
        "autor",
    )

    list_select_related = (
        "categoria",
        "institucion",
        "tipo",
    )

    date_hierarchy = "fecha"

    ordering = (
        "-anio",
        "-fecha",
    )


# ==========================================================
# ORDEN PERSONALIZADO DE LOS MODELOS EN EL ADMIN
# ==========================================================

_original_get_app_list = admin.site.get_app_list


def get_app_list(request, app_label=None):
    app_list = _original_get_app_list(request, app_label)

    orden_biblioteca = {
        "Categoria": 1,
        "Institucion": 2,
        "TipoDocumento": 3,
        "Documento": 4,
    }

    for app in app_list:
        if app["app_label"] == "biblioteca":

            app["models"].sort(
                key=lambda model: orden_biblioteca.get(
                    model["object_name"],
                    999
                )
            )

    return app_list


admin.site.get_app_list = get_app_list