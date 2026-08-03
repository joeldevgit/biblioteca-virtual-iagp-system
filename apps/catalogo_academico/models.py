from django.db import models


class Curso(models.Model):

    TIPO_EVENTO = [
        ("vivo", "Evento en Vivo"),
        ("virtual", "Evento Virtual"),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    imagen = models.ImageField(
        upload_to="cursos/",
        blank=True,
        null=True
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_EVENTO,
        default="vivo"
    )

    horas = models.PositiveIntegerField(default=120)

    semanas = models.PositiveIntegerField(default=7)

    fecha_inicio = models.DateField()

    activo = models.BooleanField(default=True)

    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.titulo