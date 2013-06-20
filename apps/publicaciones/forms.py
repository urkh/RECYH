from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget



class FormPublicaciones(ModelForm):
    class Meta:
        widgets = {
            'resumen': RedactorWidget,
            'contenido':  CKEditorWidget(editor_options={'language': 'es', 'toolbar': 'Full'}),
        }
