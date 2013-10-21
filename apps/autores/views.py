from django.shortcuts import render_to_response, get_object_or_404

from apps.autores.models import Autores
from apps.articulos.models import Articulos

#def autor(request):
def autor(request, id):

    id = int(id)
    autor = get_object_or_404(Autores, id=id)
    lineas_inv = autor.lineas_inv.all()
    articulos = Articulos.objects.filter(autor=id).order_by('-fecha_pub')[:3]
    cant_art = Articulos.objects.filter(autor=id).count()
    autores = Autores.objects.all()[:4]

    return render_to_response('front/autor.html', {'autor': autor, 'articulos': articulos, 'lineas_inv': lineas_inv, 'cant_art': cant_art, 'autores':autores})	
    #return render_to_response('front/autor.html')  



def autores(request):

    #autores = Autores.objects.annotate(cantPub=Count('autor'))
    autores = Autores.objects.all().order_by('-fecha_reg')
    return render_to_response('front/autores.html', {'autores': autores})






def autores_list(request):

    #autores = Autores.objects.annotate(cantPub=Count('autor'))
    autores = Autores.objects.all().order_by('-fecha_reg')
    return render_to_response('admin/autores.html', {'autores': autores})


def autor_edit(request, id):

    #autores = Autores.objects.annotate(cantPub=Count('autor'))
    autores = Autores.objects.all().order_by('-fecha_reg')
    return render_to_response('admin/autor.html', {'autores': autores})


def autor_add(request):
    return render_to_response('admin/autor.html')