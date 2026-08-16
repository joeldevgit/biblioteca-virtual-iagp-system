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