from django.conf.urls import patterns, include, url
#from django.contrib import admin
from django.conf import settings

#admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/$', 'apps.inicio.views.dashboard'),
    url(r'^$', 'apps.inicio.views.inicio'),
    
    url(r'^articulo/$', 'apps.articulos.views.articulo'),
    url(r'^articulos/$', 'apps.articulos.views.articulos'),
    
    url(r'^revistas/$', 'apps.revistas.views.revistas'),
    
    url(r'^autor/$', 'apps.autores.views.autor'),
    url(r'^autores/$', 'apps.autores.views.autores'),
    

    #url(r'^$', 'apps.inicio.views.inicio'),
   
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    #url(r'^autores/(\d+)/$', 'apps.autores.views.autor'),
    
    #url(r'^publicaciones/(\d+)/$', 'apps.publicaciones.views.publicacion'),
    


)
