from django.db import models
from django.utils.timezone import now
#Modelo de Usuarios - Contine todos los usuarios
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ["-created"] #- para que lo ordene del mas nuevo al mas viejo
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")    
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imágen", upload_to="blog", null=True, blank=True)
    #En caso de que se borre el usuario, se borra la entrada también
    author = models.ForeignKey (User, verbose_name="Author", on_delete=models.CASCADE)
    categories = models.ManyToManyField (Category, verbose_name="Categorías", related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ["-created"] #- para que lo ordene del mas nuevo al mas viejo
    
    def __str__(self):
        return self.title