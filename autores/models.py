from django.db import models
from PIL import Image


# Create your models here.


class Autores(models.Model):


    class Meta:
        db_table='autores'
        verbose_name_plural='Autores'


    #id
    cedula = models.CharField(max_length=12)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNac = models.DateField()
    sexo = models.IntegerField(choices=((0, 'Masculino'), (1, 'Femenino')))
    fechaReg = models.DateField()
    informacion = models.TextField()
    correo = models.EmailField()
    telefono = models.IntegerField()
    twitter = models.CharField(max_length=50) 
    facebook = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='autores')

    def __unicode__(self):
        return self.nombre


