from django import forms
from django_select2 import *
from .models import Autores
from apps.opciones.models import GradosAc, Profesiones, LineasInv
from suit.widgets import *
from suit_redactor.widgets import RedactorWidget

class GradosAcSelect(AutoModelSelect2Field):
    queryset = GradosAc.objects
    #search_fields = ('nombre__icontains',)

class ProfesionesSelect(AutoModelSelect2Field):
    queryset = Profesiones.objects
    #search_fields = ('nombre__icontains',)


class LineasInvSelect(AutoModelSelect2MultipleField):
    queryset = LineasInv.objects


class FormAutores(forms.ModelForm):
    gradoAc = GradosAcSelect(
        label = 'Grado Academico',
        widget = Select2Widget(select2_options={'width': '220px'}),
    )
    
    profesion = ProfesionesSelect(
        widget = Select2Widget(select2_options={'width': '220px'}),
    )

    lineasInv = LineasInvSelect(
        label = 'Lineas de Investigacion',
        widget = Select2MultipleWidget(select2_options={'width': '220px'}),
    )

    class Meta:
        model = Autores
        widgets = {
            'informacion': RedactorWidget(
                editor_options={
                    'buttons': ['html', '|', 'bold', 'italic'],
                    'lang': 'es'
                }
            ),
            'sexo': Select2Widget(select2_options={'width':'200px'}),
            'fechaNac': SuitDateWidget(),
            'fechaReg': SuitDateWidget(),
            'telefono': EnclosedInput(append='icon-signal'),
            'twitter': EnclosedInput(prepend='@'),
            'facebook': EnclosedInput(prepend='icon-thumbs-up'),
            'correo': EnclosedInput(append='icon-envelope'),
        }
    

