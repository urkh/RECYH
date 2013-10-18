from PIL import Image
from django.db import models

# Create your models here.

class Areas(models.Model):
    class Meta:
        verbose_name_plural='Areas'

    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='areas', blank=True, null=True)

    def __unicode__(self):
        return self.nombre
        

class Categorias(models.Model):
    class Meta:
        verbose_name_plural='Categorias'

    area = models.ForeignKey(Areas)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class LineasInv(models.Model):
    class Meta:
        verbose_name_plural='Lineas de Investigacion'

    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class Profesiones(models.Model):
    class Meta:
        verbose_name_plural='Profesiones'
       
    
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class GradosAc(models.Model):
    class Meta:
        verbose_name_plural='Grados Academicos'

    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Suscripciones(models.Model):
    class Meta:
        verbose_name_plural = 'Suscripciones'

    correo = models.EmailField()
    fecha = models.DateField()

    def __unicode__(self):
        return self.correo
