from django.db import models
from django.utils.text import slugify
import re


# =========================================================
# INSTITUCIÓN
# =========================================================
class Institucion(models.Model):

    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre"
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True
    )

    imagen_url = models.URLField(
        blank=True,
        verbose_name="URL de imagen Google Drive"
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    orden = models.PositiveIntegerField(
        default=0,
        verbose_name="Orden"
    )

    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"
        ordering = ["orden", "nombre"]

    def save(self, *args, **kwargs):

        # Generar slug automáticamente
        if not self.slug:
            self.slug = slugify(self.nombre)

        # Convertir automáticamente Google Drive
        if self.imagen_url:

            match = re.search(
                r"/file/d/([^/]+)",
                self.imagen_url
            )

            if match:

                archivo_id = match.group(1)

                self.imagen_url = (
                    f"https://drive.google.com/thumbnail"
                    f"?id={archivo_id}&sz=w1000"
                )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


# =========================================================
# JURISPRUDENCIA
# =========================================================
class Jurisprudencia(models.Model):

    TIPOS = [
        ("opinion", "Opinión"),
        ("pronunciamiento", "Pronunciamiento"),
    ]

    # ==========================================
    # INSTITUCIÓN
    # ==========================================
    institucion = models.ForeignKey(
        Institucion,
        on_delete=models.CASCADE,
        related_name="jurisprudencias",
        verbose_name="Institución"
    )

    # ==========================================
    # TIPO DE DOCUMENTO
    # ==========================================
    tipo = models.CharField(
        max_length=30,
        choices=TIPOS,
        default="opinion",
        verbose_name="Tipo"
    )

    # ==========================================
    # INFORMACIÓN
    # ==========================================
    titulo = models.CharField(
        max_length=255,
        verbose_name="Título"
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True
    )

    tema = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Tema"
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )

    # ==========================================
    # PDF
    # ==========================================
    pdf_url = models.URLField(
        verbose_name="URL del PDF"
    )

    # ==========================================
    # FECHA
    # ==========================================
    fecha = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha"
    )

    año = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Año"
    )

    # ==========================================
    # ESTADO
    # ==========================================
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Jurisprudencia"
        verbose_name_plural = "Jurisprudencias"
        ordering = ["-año", "-created_at"]

    def save(self, *args, **kwargs):

        # Generar slug automáticamente
        if not self.slug:
            self.slug = slugify(self.titulo)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo