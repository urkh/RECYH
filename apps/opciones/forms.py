from django import forms
from django_select2 import *
from suit.widgets import *
from .models import Areas, Categorias


class AreasSelect(AutoModelSelect2Field):
    queryset = Areas.objects
    search_fields = ('nombre__icontains', )



class FormCategorias(forms.ModelForm):

    area = AreasSelect()

    class Meta:
        model = Categorias



class FormAreas(forms.ModelForm):
    class Meta:
        widgets = {
            'nombre': EnclosedInput(append='icon-pencil'),

        }

