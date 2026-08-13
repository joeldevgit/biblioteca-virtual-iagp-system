from django.contrib import admin
from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "tipo",
        "fecha_inicio",
        "activo",
        "orden",
    )

    list_filter = (
        "tipo",
        "activo",
    )

    search_fields = (
        "titulo",
    )