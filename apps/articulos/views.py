from django.shortcuts import render_to_response, get_object_or_404

from apps.articulos.models import Articulos, Comentarios



def articulo(request, id):
    
    id=int(id)
    articulo = get_object_or_404(Articulos, id=id)
    comentarios = Comentarios.objects.filter(articulo=id)
    cant_art = Articulos.objects.filter(autor=articulo.autor.id).count()

    #contenidos = list(procesarContenido(publicacion.contenido, 50))

    #print contenidos
    #print publicacion.contenido
    
    return render_to_response('front/articulo.html', {'articulo': articulo, 'comentarios': comentarios, 'cant_art': cant_art})




def articulos(request):
    articulos = Articulos.objects.all()
    return render_to_response('front/articulos.html', {'articulos':articulos})



def procesarContenido(contenido, numero):
    while contenido:
        yield contenido[:numero]
        contenido = contenido[numero:]