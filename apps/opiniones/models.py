from django.db import models


class Opinion(models.Model):

    opinion = models.CharField(
        max_length=200,
        verbose_name="Opinión"
    )

    tema = models.TextField(
        verbose_name="Tema"
    )

    fecha = models.DateField(
        verbose_name="Fecha"
    )

    anio = models.PositiveIntegerField(
        verbose_name="Año"
    )

    pdf = models.URLField(
        max_length=500,
        verbose_name="Enlace PDF"
    )


    class Meta:
        verbose_name = "Opinión"
        verbose_name_plural = "Opiniones"
        ordering = ["-anio", "-fecha"]

    def __str__(self):
        return self.opinion