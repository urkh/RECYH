from autores.models import Autores
from django.contrib import admin


class AdminAutores(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'correo')


admin.site.register(Autores, AdminAutores)
