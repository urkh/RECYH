from django.conf.urls import patterns, include, url
#from django.contrib import admin
from django.conf import settings

#admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/$', 'apps.admin.inicio.views.inicio'),
    url(r'^$', 'apps.front.inicio.views.inicio'),
    url(r'^articulos/$', 'apps.front.publicaciones.views.publicaciones'),
    url(r'^revistas/$', 'apps.front.revistas.views.revistas'),
    url(r'^autores/$', 'apps.front.autores.views.autores'),

    #url(r'^$', 'apps.inicio.views.inicio'),
   
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    #url(r'^autores/(\d+)/$', 'apps.autores.views.autor'),
    
    #url(r'^publicaciones/(\d+)/$', 'apps.publicaciones.views.publicacion'),
    


)
