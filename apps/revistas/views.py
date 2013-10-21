from django.shortcuts import render_to_response

def revistas(request):
    #publicaciones = Publicaciones.objects.all()
    return render_to_response('front/revistas.html')
