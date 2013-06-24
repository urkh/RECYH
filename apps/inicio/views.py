# Create your views here.
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.autores.models import Autores
from apps.publicaciones.models import Publicaciones, Comentarios
from apps.opciones.models import Categorias
from django.db.models import Count



def inicio(request):
    autores = Autores.objects.annotate(cantPub=Count('autores')).order_by('-fechaReg')[:3]
    publicaciones = Publicaciones.objects.all().order_by('-fechaReg')[:4]
    comentarios = Comentarios.objects.all().order_by('-fecha')[:3]
    categorias = Categorias.objects.all()

    return render_to_response('inicio.html',{'autores': autores, 'publicaciones': publicaciones, 'comentarios': comentarios, 'categorias': categorias}, context_instance=RequestContext(request))

