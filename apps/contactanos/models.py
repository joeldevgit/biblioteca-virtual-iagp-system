from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    departamento = models.CharField(max_length=100)
    compania = models.CharField(max_length=150, blank=True)
    movil = models.CharField(max_length=20)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre