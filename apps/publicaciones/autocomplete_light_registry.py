import autocomplete_light

from apps.autores.models import Autores

autocomplete_light.register(Autores, search_fields=('nombre',),
    autocomplete_js_attributes={'placeholder': 'buscar'})
