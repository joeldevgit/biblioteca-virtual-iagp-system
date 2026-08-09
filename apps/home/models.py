from django.db import models

class Testimonio(models.Model):
    nombre = models.CharField(max_length=150)
    profesion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    comentario = models.TextField()
    foto = models.ImageField(upload_to="testimonios/")
    calificacion = models.PositiveSmallIntegerField(default=5)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.nombre