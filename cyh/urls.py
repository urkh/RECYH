from django.conf.urls import patterns, include, url
#from django.contrib import admin
from django.conf import settings

#admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', 'apps.admin.inicio.views.inicio'),
   

    #url(r'^$', 'apps.inicio.views.inicio'),
   
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    #url(r'^autores/(\d+)/$', 'apps.autores.views.autor'),
    #url(r'^autores/lista/$', 'apps.autores.views.lista'),
    #url(r'^publicaciones/(\d+)/$', 'apps.publicaciones.views.publicacion'),
    #url(r'^publicaciones/lista/$', 'apps.publicaciones.views.lista'),


)
