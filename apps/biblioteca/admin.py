from django.contrib import admin
from .models import Institucion, Jurisprudencia


# =========================================================
# INSTITUCIONES
# =========================================================
@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "orden",
        "activo",
    )

    list_filter = (
        "activo",
    )

    search_fields = (
        "nombre",
    )

    prepopulated_fields = {
        "slug": ("nombre",)
    }

    ordering = (
        "orden",
        "nombre",
    )

    list_per_page = 20


# =========================================================
# JURISPRUDENCIAS
# =========================================================
@admin.register(Jurisprudencia)
class JurisprudenciaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "institucion",
        "tipo",
        "tema",
        "fecha",
        "año",
        "activo",
    )

    list_filter = (
        "institucion",
        "tipo",
        "año",
        "activo",
    )

    search_fields = (
        "titulo",
        "tema",
        "descripcion",
    )

    prepopulated_fields = {
        "slug": ("titulo",)
    }

    ordering = (
        "-año",
        "-fecha",
    )

    list_per_page = 20