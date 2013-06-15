# Create your views here.
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from autores.models import Autores
from publicaciones.models import Publicaciones, Comentarios



def inicio(request):
    autores = Autores.objects.all().order_by('-fechaReg')[:3]
    publicaciones = Publicaciones.objects.all().order_by('-fechaReg')[:4]
    comentarios = Comentarios.objects.all().order_by('-fecha')[:3]

    return render_to_response('inicio.html',{'autores': autores, 'publicaciones': publicaciones, 'comentarios': comentarios}, context_instance=RequestContext(request))

