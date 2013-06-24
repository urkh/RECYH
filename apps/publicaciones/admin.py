from apps.publicaciones.models import Publicaciones, Comentarios
from apps.autores.models import Autores
from apps.publicaciones.forms import FormPublicaciones

from django.contrib import admin

class AdminPublicaciones(admin.ModelAdmin):
    
    form = FormPublicaciones
    list_display = ('categoria', 'titulo', 'fechaPub', 'lecturas', 'getAutores')
    list_filter = ('categoria__nombre','numero')
    search_fields = ('categoria__nombre', 'numero')
    date_hierarchy = 'fechaPub'
    #exclude = ('lecturas',)
    fieldsets = [
        (None, {'fields':['categoria', 'autores', 'fechaReg', 'informacion']}),
        ('Datos de la publicacion', {'fields': ['titulo', 'fechaPub', 'resumen', 'numero', 'foto', 'lecturas']}),
        ('Contenido', {'fields':['contenido', ]})
    
    ]



class AdminComentarios(admin.ModelAdmin):
    list_display = ('publicacion', 'fecha')


admin.site.register(Publicaciones, AdminPublicaciones)
admin.site.register(Comentarios, AdminComentarios)
