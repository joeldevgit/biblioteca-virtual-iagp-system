from django.contrib import admin
from .models import Testimonio

@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "profesion",
        "ciudad",
        "calificacion",
        "orden",
        "activo",
    )
    list_editable = (
        "orden",
        "activo",
    )