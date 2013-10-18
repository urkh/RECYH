# Create your views here
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.front.publicaciones.models import Publicaciones, Comentarios






def publicacion(request, ids):
    
    ids=int(ids)
    publicacion = Publicaciones.objects.get(id=ids)
    autores = publicacion.autores.all()
    comentarios = Comentarios.objects.filter(publicacion=ids)



    contenidos = list(procesarContenido(publicacion.contenido, 50))

    #print contenidos
    #print publicacion.contenido
    








    return render_to_response('publicacion.html', {'publicacion': publicacion, 'comentarios': comentarios, 'autores': autores, 'contenidos': contenidos}, context_instance=RequestContext(request))




def procesarContenido(contenido, numero):
    while contenido:
        yield contenido[:numero]
        contenido = contenido[numero:]
 

def publicaciones(request):
    #publicaciones = Publicaciones.objects.all()
    return render_to_response('front/publicaciones.html')
