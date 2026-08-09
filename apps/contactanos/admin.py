from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "departamento", "fecha", "atendido")
    list_filter = ("atendido", "departamento")
    search_fields = ("nombre", "email")