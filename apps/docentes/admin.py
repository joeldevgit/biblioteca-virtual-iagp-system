from django.contrib import admin
from .models import Docente


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo", "orden")
    list_filter = ("activo",)
    search_fields = ("nombre",)
    list_editable = ("activo", "orden")