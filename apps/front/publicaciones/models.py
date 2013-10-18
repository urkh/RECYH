from django.db import models
from apps.front.autores.models import Autores
from apps.front.opciones.models import Categorias
from PIL import Image

# Create your models here.


class Publicaciones(models.Model):

    class Meta:
        db_table='publicaciones'
        verbose_name_plural='Publicaciones'


    categoria = models.ForeignKey(Categorias)
    autores = models.ManyToManyField(Autores, related_name='autores')
    titulo = models.CharField(max_length=100)
    fechaReg = models.DateField('Fecha de Registro')
    fechaPub = models.DateField('Fecha de Publicacion')
    informacion = models.TextField()
    numero = models.IntegerField('Numero de Publicacion')
    resumen = models.TextField()
    contenido = models.TextField()
    lecturas = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='publicaciones', blank=True, null=True)

    def __unicode__(self):
        return self.titulo

    def getAutores(self):
        #autoress = autores.nombre + autores.apellido
        return ', '.join([autores.nombre for autores in self.autores.all()])
        #return '%s'%(obj.autores.nombre)


    getAutores.short_description = 'Autores'
    getAutores.admin_order_field = 'autores__cedula'





class Comentarios(models.Model):

    class Meta:
        db_table='comentarios_pub'
        verbose_name_plural='Comentarios'


    publicacion = models.ForeignKey(Publicaciones)
    comentario = models.TextField()
    fecha = models.DateField()

    def __unicode__(self):
        return self.comentario
