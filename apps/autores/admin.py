from .models import Autores
from .forms import FormAutores
from django.contrib import admin


class AdminAutores(admin.ModelAdmin):
    form = FormAutores
    list_filter = ('cedula',)
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'correo')
    search_fields = ('cedula', 'nombre', 'apellido')
    date_hierarchy = 'fechaReg'
    fieldsets = [
        (None, {'fields': ['gradoAc', 'profesion', 'lineasInv']}),
        ('Datos Personales', {'fields': ['cedula', 'nombre', 'apellido', 'sexo','fechaNac']}),
        ('Datos de Contacto', {'fields': ['telefono', 'correo', 'twitter', 'facebook']}),
        ('Otros datos', {'fields': ['fechaReg', 'informacion', 'foto']})
        
    ]


admin.site.register(Autores, AdminAutores)
