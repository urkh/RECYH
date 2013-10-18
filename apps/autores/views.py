# Create your views here
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count

from apps.autores.models import Autores
from apps.articulos.models import Publicaciones

def autor(request):
#def autor(request, ids):

    #ids = int(ids)
    #autor = Autores.objects.get(id=ids)
    #lineasInv = autor.lineasInv.all()
    #publicaciones = Publicaciones.objects.filter(autores=ids)

    #return render_to_response('autor.html', {'autor': autor, 'publicaciones': publicaciones, 'lineasInv': lineasInv}, context_instance=RequestContext(request))	
    return render_to_response('front/autor.html')  



def autores(request):

    autores = Autores.objects.annotate(cantPub=Count('autores'))
    #return render_to_response('listaAutores.html', {'autores': autores}, context_instance=RequestContext(request))
    return render_to_response('front/autores.html')