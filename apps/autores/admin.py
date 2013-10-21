from apps.autores.models import Autores
from apps.autores.forms import FormAutores
from django.contrib import admin


class AdminAutores(admin.ModelAdmin):
    #form = FormAutores
    list_filter = ('cedula',)
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'correo')
    search_fields = ('cedula', 'nombre', 'apellido')
    date_hierarchy = 'fecha_reg'
    
    """
    fieldsets = [
        ('Informacion Profesional', {'classes': ('suit-tab suit-tab-informacion', ), 'fields': ['grado_ac', 'profesion', 'lineas_inv']}),
        ('Datos Personales', {'classes': ('suit-tab suit-tab-datos_p', ), 'fields': ['cedula', 'nombre', 'apellido', 'sexo','fecha_nac']}),
        ('Datos de Contacto', {'classes': ('suit-tab suit-tab-datos_c', ), 'fields': ['telefono', 'correo', 'twitter', 'facebook', 'linkedln']}),
        ('Otros datos', {'classes': ('suit-tab suit-tab-datos_o', ), 'fields': ['fecha_reg', 'informacion', 'foto']})
        
    ]
    """
    fieldsets = [
        ('Informacion Profesional', {'fields': ['grado_ac', 'profesion', 'lineas_inv']}),
        ('Datos Personales', {'fields': ['cedula', 'nombre', 'apellido', 'sexo','fecha_nac']}),
        ('Datos de Contacto', {'fields': ['telefono', 'correo', 'twitter', 'facebook', 'linkedin']}),
        ('Otros datos', {'fields': ['fecha_reg', 'informacion', 'foto']})
        
    ]
    #suit_form_tabs = (('informacion', 'Informacion Profesional'), ('datos_p', 'Datos Personales'), ('datos_c', 'Contacto'), ('datos_o', 'Otros datos'))


admin.site.register(Autores, AdminAutores)
