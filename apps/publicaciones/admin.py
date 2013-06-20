from apps.publicaciones.models import Publicaciones, Comentarios
from apps.autores.models import Autores
from apps.publicaciones.forms import FormPublicaciones

from django.contrib import admin
import autocomplete_light

class AdminPublicaciones(admin.ModelAdmin):
    
    form = FormPublicaciones
    list_display = ('categoria', 'autores', 'titulo', 'fechaPub', 'issn', 'lecturas')
    list_display_links = ('autores', )
    list_filter = ('categoria__nombre','issn')
    search_fields = ('categoria__nombre', 'issn')
    date_hierarchy = 'fechaPub'
    #exclude = ('lecturas',)

autocomplete_light.register(Autores, search_fields=('nombre',),
    autocomplete_js_attributes={'placeholder': 'city name ..'})




class AdminComentarios(admin.ModelAdmin):
    list_display = ('publicacion', 'fecha')


admin.site.register(Publicaciones, AdminPublicaciones)
admin.site.register(Comentarios, AdminComentarios)
