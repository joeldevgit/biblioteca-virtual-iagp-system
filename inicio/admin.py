from django.contrib import admin
from .models import Hero, Servicio, Contador, About, Portfolio, Skill, Testimonio, BlogPost, PartnerLogo, ContactMessage


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto_boton")


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "orden", "activo")
    list_editable = ("orden", "activo")


@admin.register(Contador)
class ContadorAdmin(admin.ModelAdmin):
    list_display = ("titulo", "numero", "orden", "activo")
    list_editable = ("numero", "orden", "activo")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto_boton")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "orden", "activo")
    list_filter = ("categoria", "activo")
    list_editable = ("orden", "activo")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("nombre", "porcentaje", "orden", "activo")
    list_editable = ("porcentaje", "orden", "activo")


@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cargo", "orden", "activo")
    list_editable = ("orden", "activo")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "fecha", "activo")
    list_filter = ("categoria", "activo")


@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "orden", "activo")
    list_editable = ("orden", "activo")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "asunto", "creado", "leido")
    list_filter = ("leido", "creado")
    search_fields = ("nombre", "email", "asunto")
    readonly_fields = ("nombre", "email", "asunto", "mensaje", "creado")
