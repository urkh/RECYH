from django.forms import ModelForm
from suit.widgets import  SuitDateWidget, EnclosedInput
from suit_ckeditor.widgets import CKEditorWidget
from django_select2 import AutoModelSelect2Field, AutoModelSelect2MultipleField, Select2MultipleWidget, AutoHeavySelect2Widget
from apps.articulos.models import Articulos
from apps.autores.models import Autores
from apps.opciones.models import Categorias



class CategoriasSelect(AutoModelSelect2Field):
    queryset = Categorias.objects
    search_fields = ('nombre__icontains',)



class AutoresSelect(AutoModelSelect2MultipleField):
    queryset = Autores.objects
    search_fields = ('nombre__icontains', 'cedula__icontains', 'apellido__icontains')




class FormArticulos(ModelForm):
    autores = AutoresSelect(
        label = 'Autores',
        widget = Select2MultipleWidget(select2_options={'width': '250px'}),
    )

    categoria = CategoriasSelect(
        label = 'Categoria',
        widget = AutoHeavySelect2Widget(select2_options={'width': '220px'}),
    )
    
    
    class Meta:

        model = Articulos




        toolbar = [
            {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup']},
            {'groups':['undo', 'clipboard']},
            {'name': 'paragraph', 'groups': ['list', 'indent', 'align']},
            #{'name': 'document', 'groups': ['mode']}, '/',
            {'name': 'styles'}, {'name': 'colors'},
            {'name': 'insert_custom', 'items': ['Image', 'Table', 'HorizontalRule', 'Maximize']}, 
        ]

        toolbar2 = [
            {'items': ['Bold', 'Italic']},
        ]
        

        config = {
            'autoGrow_onStartup': True,
            'autoGrow_minHeight': 100,
            'autoGrow_maxHeight': 250,
            'extraPlugins': 'autogrow',
            'language': 'es',
            'toolbarGroups': toolbar
        }


        config2 = {
            'language': 'es',
            'toolbar': toolbar2
        
        }
        


        widgets = {
            'fecha_reg': SuitDateWidget(),
            'fecha_pub': SuitDateWidget(),
            'numero': EnclosedInput(append='icon-list', attrs={'class': 'input-small'}),
            'resumen': CKEditorWidget(editor_options=config2),

            'informacion': CKEditorWidget(editor_options=config2),
            
            'contenido':  CKEditorWidget(editor_options=config),
        }
