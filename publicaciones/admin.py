from publicaciones.models import Publicaciones, Comentarios
from django.contrib import admin

class AdminPublicaciones(admin.ModelAdmin):
    list_display = ('categoria', 'autores', 'titulo', 'fechaPub', 'issn', 'lecturas')
    list_filter = ('categoria__nombre','issn')
    search_fields = ('categoria__nombre', 'issn')
    date_hierarchy = 'fechaPub'


class AdminComentarios(admin.ModelAdmin):
    list_display = ('publicacion', 'fecha')

admin.site.register(Publicaciones, AdminPublicaciones)
admin.site.register(Comentarios, AdminComentarios)
