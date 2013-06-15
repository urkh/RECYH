from django.db import models
from PIL import Image
# Create your models here.

class Areas(models.Model):
    
    class Meta:
        db_table='areas'
        verbose_name_plural='Areas'

    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='areas')

    def __unicode__(self):
        return self.nombre


