from django.db import models
from apps.areas.models import Areas

# Create your models here.

class Categorias(models.Model):
    
    class Meta:
        db_table='categorias'
        verbose_name_plural='Categorias'

    area = models.ForeignKey(Areas)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre
