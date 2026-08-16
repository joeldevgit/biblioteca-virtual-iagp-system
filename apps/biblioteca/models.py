from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Institucion(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    sigla = models.CharField(max_length=30, blank=True)

    imagen = models.ImageField(
        upload_to="biblioteca/instituciones/",
        blank=True,
        null=True
    )

    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"
        ordering = ["nombre"]

    def __str__(self):
        if self.sigla:
            return f"{self.nombre} ({self.sigla})"
        return self.nombre


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="tipos_documento"
    )
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"
        ordering = ["categoria", "nombre"]
        constraints = [
            models.UniqueConstraint(
                fields=["categoria", "nombre"],
                name="unique_tipo_documento_categoria"
            )
        ]

    def __str__(self):
        return f"{self.categoria.nombre} → {self.nombre}"


class Documento(models.Model):
    titulo = models.CharField(max_length=300)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="documentos"
    )

    institucion = models.ForeignKey(
        Institucion,
        on_delete=models.PROTECT,
        related_name="documentos",
        blank=True,
        null=True
    )

    tipo = models.ForeignKey(
        TipoDocumento,
        on_delete=models.PROTECT,
        related_name="documentos"
    )

    autor = models.CharField(max_length=200, blank=True)

    tema = models.CharField(max_length=300, blank=True)

    descripcion = models.TextField(blank=True)

    fecha = models.DateField(blank=True, null=True)

    anio = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    pdf = models.FileField(
        upload_to="biblioteca/documentos/",
        blank=True,
        null=True
    )

    pdf_url = models.URLField(
        blank=True
    )

    activo = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ["-anio", "-fecha", "-id"]

    def __str__(self):
        return self.titulo