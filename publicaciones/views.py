# Create your views here
from django.shortcuts import render_to_response
from django.template import RequestContext

from publicaciones.models import Publicaciones, Comentarios


def publicacion(request, ids):
    ids=int(ids)

    publicacion = Publicaciones.objects.get(id=ids)
    comentarios = Comentarios.objects.filter(publicacion=ids)


    return render_to_response('publicacion.html', {'publicacion': publicacion, 'comentarios': comentarios}, context_instance=RequestContext(request))


def lista(request):
    publicaciones = Publicaciones.objects.all()
    return render_to_response('listaPublicaciones.html', {'publicaciones': publicaciones}, context_instance=RequestContext(request))
