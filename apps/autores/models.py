from PIL import Image
from django.db import models
from apps.opciones.models import GradosAc, Profesiones, LineasInv


class Autores(models.Model):

    class Meta:
        verbose_name_plural='Autores'
  
    grado_ac = models.ForeignKey(GradosAc)
    profesion = models.ForeignKey(Profesiones)
    lineas_inv = models.ManyToManyField(LineasInv)
    
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField('Fecha de Nacimiento')
    sexo = models.IntegerField(choices=((0, 'Masculino'), (1, 'Femenino')))
    fecha_reg = models.DateField('Fecha de Registro')
    informacion = models.TextField()
    correo = models.EmailField()
    telefono = models.IntegerField()
    twitter = models.CharField(max_length=50) 
    facebook = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='img/autores', blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    def getLineasInv(self):
        return ', '.join([lineas_inv.nombre for lineas_inv in self.lineas_inv.all()])
