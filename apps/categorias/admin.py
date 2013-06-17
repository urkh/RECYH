from apps.categorias.models import Categorias
from django.contrib import admin


class AdminCategorias(admin.ModelAdmin):
    list_display = ('nombre', 'area')


admin.site.register(Categorias, AdminCategorias)
