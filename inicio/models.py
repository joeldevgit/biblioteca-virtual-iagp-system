from django.db import models


class Hero(models.Model):
    titulo = models.CharField(max_length=200, default="We are a full service digital company")
    subtitulo = models.CharField(max_length=300, default="Lorem ipsum dolor sit amet, consectetur adipisicing elit")
    texto_boton = models.CharField(max_length=80, default="Learn More")
    enlace_boton = models.CharField(max_length=200, default="#")
    imagen_fondo = models.ImageField(upload_to="hero/", blank=True, null=True)

    class Meta:
        verbose_name = "Hero principal"
        verbose_name_plural = "Hero principal"

    def __str__(self):
        return self.titulo


class Servicio(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    icono = models.ImageField(upload_to="servicios/", blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.titulo


class Contador(models.Model):
    titulo = models.CharField(max_length=100)
    numero = models.PositiveIntegerField(default=0)
    icono = models.ImageField(upload_to="contadores/", blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "Contador"
        verbose_name_plural = "Contadores"

    def __str__(self):
        return self.titulo


class About(models.Model):
    titulo = models.CharField(max_length=200, default="We create amazing digital products")
    descripcion = models.TextField()
    texto_boton = models.CharField(max_length=80, default="Learn More")
    enlace_boton = models.CharField(max_length=200, default="#")
    imagen = models.ImageField(upload_to="about/", blank=True, null=True)

    class Meta:
        verbose_name = "Sección About"
        verbose_name_plural = "Sección About"

    def __str__(self):
        return self.titulo


class Portfolio(models.Model):
    CATEGORIAS = (
        ("branding", "Branding"),
        ("webtemplate", "Web Template"),
        ("seo", "SEO"),
        ("digital", "Digital Marketing"),
    )
    titulo = models.CharField(max_length=120, default="View Project")
    categoria = models.CharField(max_length=30, choices=CATEGORIAS, default="branding")
    imagen = models.ImageField(upload_to="portfolio/")
    enlace = models.CharField(max_length=200, default="#")
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.titulo


class Skill(models.Model):
    nombre = models.CharField(max_length=100)
    porcentaje = models.PositiveIntegerField(default=0)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.nombre


class Testimonio(models.Model):
    nombre = models.CharField(max_length=120)
    cargo = models.CharField(max_length=150)
    comentario = models.TextField()
    foto = models.ImageField(upload_to="testimonios/", blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"

    def __str__(self):
        return self.nombre


class BlogPost(models.Model):
    titulo = models.CharField(max_length=160)
    categoria = models.CharField(max_length=80, default="Agency")
    resumen = models.TextField()
    imagen = models.ImageField(upload_to="blog/", blank=True, null=True)
    fecha = models.DateField()
    enlace = models.CharField(max_length=200, default="#")
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["-fecha", "id"]
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.titulo


class PartnerLogo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="partners/")
    enlace = models.CharField(max_length=200, default="#")
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["orden", "id"]
        verbose_name = "Logo partner"
        verbose_name_plural = "Logos partners"

    def __str__(self):
        return self.nombre


class ContactMessage(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    asunto = models.CharField(max_length=160)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ["-creado"]
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"
