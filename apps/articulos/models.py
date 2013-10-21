from PIL import Image
from django.db import models
from apps.autores.models import Autores
from apps.opciones.models import Categorias


# Create your models here.


class Articulos(models.Model):

    class Meta:
        verbose_name_plural='Articulos'

    categoria = models.ForeignKey(Categorias)
    autor = models.ForeignKey(Autores)
    titulo = models.CharField(max_length=100)
    fecha_pub = models.DateField('Fecha de Publicacion')
    informacion = models.TextField()
    resumen = models.TextField()
    contenido = models.TextField()
    lecturas = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='img/articulos', blank=True, null=True)

    def __unicode__(self):
        return self.titulo

    #def getAutores(self):
    #autoress = autores.nombre + autores.apellido
    #return ', '.join([autores.nombre for autores in self.autores.all()])
    #return '%s'%(obj.autores.nombre)


    #getAutores.short_description = 'Autores'
    #getAutores.admin_order_field = 'autores__cedula'





class Comentarios(models.Model):

    class Meta:
        verbose_name_plural='Comentarios'

    articulo = models.ForeignKey(Articulos)
    nombre = models.CharField(max_length=20)
    comentario = models.CharField(max_length=200)
    fecha = models.DateField()

    def __unicode__(self):
        return self.comentario
