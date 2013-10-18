from apps.opciones.models import GradosAc, Profesiones, LineasInv

from django.db import models
from PIL import Image


# Create your models here.


class Autores(models.Model):


    class Meta:
        verbose_name_plural='Autores'


    #id
    
    gradoAc = models.ForeignKey(GradosAc)
    profesion = models.ForeignKey(Profesiones)
    lineasInv = models.ManyToManyField(LineasInv)
    
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNac = models.DateField('Fecha de Nacimiento')
    sexo = models.IntegerField(choices=((0, 'Masculino'), (1, 'Femenino')))
    fechaReg = models.DateField('Fecha de Registro')
    informacion = models.TextField()
    correo = models.EmailField()
    telefono = models.IntegerField()
    twitter = models.CharField(max_length=50) 
    facebook = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='autores', blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    def getLineasInv(self):
        return ', '.join([lineasInv.nombre for lineasInv in self.lineasInv.all()])
