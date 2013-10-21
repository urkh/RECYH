from apps.articulos.models import Articulos, Comentarios
from apps.autores.models import Autores
from apps.articulos.forms import FormArticulos

from django.contrib import admin

class AdminArticulos(admin.ModelAdmin):
    
    #form = FormArticulos
    list_display = ('categoria', 'titulo', 'fecha_pub')
    list_filter = ('categoria__nombre',)
    search_fields = ('categoria__nombre',)
    date_hierarchy = 'fecha_pub'
    #exclude = ('lecturas',)
    fieldsets = [
        ('Categoria', {'classes': ('suit-tab suit-tab-categoria', ), 'fields':['categoria', 'autor', 'informacion']}),
        ('Datos de la publicacion', {'classes': ('suit-tab suit-tab-datos',), 'fields': ['titulo', 'fecha_pub', 'resumen', 'foto', 'lecturas']}),
        ('Contenido', {'classes':('suit-tab suit-tab-contenido',), 'fields':['contenido', ]})
    
    ]

    suit_form_tabs = (('categoria', 'Informacion'), ('datos', 'Datos'), ('contenido', 'Contenido'))




class AdminComentarios(admin.ModelAdmin):
    list_display = ('articulo', 'fecha')


admin.site.register(Articulos, AdminArticulos)
admin.site.register(Comentarios, AdminComentarios)
