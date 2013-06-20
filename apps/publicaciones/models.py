from django.db import models
from apps.autores.models import Autores
from apps.opciones.models import Categorias
from PIL import Image

# Create your models here.


class Publicaciones(models.Model):

    class Meta:
        db_table='publicaciones'
        verbose_name_plural='Publicaciones'


    categoria = models.ForeignKey(Categorias)
    autores = models.ForeignKey(Autores)
    titulo = models.CharField(max_length=100)
    fechaReg = models.DateField()
    fechaPub = models.DateField()
    issn = models.CharField('ISSN', max_length=50)
    isbn = models.CharField('ISBN', max_length=50)
    informacion = models.TextField()
    resumen = models.TextField()
    contenido = models.TextField()
    lecturas = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='publicaciones')

    def __unicode__(self):
        return self.titulo





class Comentarios(models.Model):

    class Meta:
        db_table='comentarios_pub'
        verbose_name_plural='Comentarios'


    publicacion = models.ForeignKey(Publicaciones)
    comentario = models.TextField()
    fecha = models.DateField()

    def __unicode__(self):
        return self.comentario
