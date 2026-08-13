from django.db import models


class Docente(models.Model):
    nombre = models.CharField(max_length=150)
    foto = models.ImageField(
        upload_to="docentes/",
        blank=True,
        null=True
    )
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden", "nombre"]
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return self.nombre