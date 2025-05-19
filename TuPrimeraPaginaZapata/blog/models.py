from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Articulo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Publicación")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='articulos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='articulos')
    imagen_destacada = models.ImageField(upload_to='articulos_imagenes/', blank=True, null=True, verbose_name="Imagen Destacada")

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_publicacion'] # Ordenar artículos por fecha de publicación descendente
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"