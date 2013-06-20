from django.contrib import admin
from .models import *
from .forms import *



class AdminAreas(admin.ModelAdmin):
    form = FormAreas
    list_filter = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(Areas, AdminAreas)   




class AdminCategorias(admin.ModelAdmin):

    form = FormCategorias
    #raw_id_fields = ('area',)
    list_display = ('nombre', 'area')
    list_filter = ('nombre',)
    search_fields = ('nombre',)

    """
    fieldsets = [
        (None,{'fields': ['nombre', 'area']}),
    ]"""
admin.site.register(Categorias, AdminCategorias)



class AdminLineasInv(admin.ModelAdmin):
    
    list_filter = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(LineasInv, AdminLineasInv)



class AdminProfesiones(admin.ModelAdmin):

    list_filter = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(Profesiones, AdminProfesiones)



class AdminSuscripciones(admin.ModelAdmin):

    list_display = ('correo', 'fecha')
    list_filter = ('correo', 'fecha')
    search_fields = ('correo', 'fecha')
    date_hierarchy = 'fecha'
admin.site.register(Suscripciones, AdminSuscripciones)




class AdminGradosAc(admin.ModelAdmin):
    list_filter = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(GradosAc, AdminGradosAc)




