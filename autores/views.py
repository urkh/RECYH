# Create your views here
from django.shortcuts import render_to_response
from django.template import RequestContext

from autores.models import Autores
from publicaciones.models import Publicaciones

def autor(request, ids):

    ids = int(ids)
    autor = Autores.objects.get(id=ids)
    publicaciones = Publicaciones.objects.filter(autores=ids)


    return render_to_response('autor.html', {'autor': autor, 'publicaciones': publicaciones}, context_instance=RequestContext(request))



def lista(request):

    autores = Autores.objects.all()
    return render_to_response('listaAutores.html', {'autores': autores}, context_instance=RequestContext(request))
