from django.contrib import admin
from .models import Opinion


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):

    list_display = (
        "opinion",
        "tema",
        "fecha",
        "anio",
        "ver_pdf",
    )

    list_filter = (
        "anio",
        "fecha",
    )

    search_fields = (
        "opinion",
        "tema",
    )

    ordering = (
        "-anio",
        "-fecha",
    )

    @admin.display(description="PDF")
    def ver_pdf(self, obj):

        if obj.pdf:
            return "Ver PDF"

        return "Sin PDF"