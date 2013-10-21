from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()



urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ds2/', include('django_select2.urls')),



    url(r'^$', 'apps.inicio.views.inicio'),
    
    url(r'^articulo/(\d+)/$', 'apps.articulos.views.articulo'),
    url(r'^articulos/$', 'apps.articulos.views.articulos'),
    
    url(r'^revistas/$', 'apps.revistas.views.revistas'),
    
    url(r'^autor/(\d+)/$', 'apps.autores.views.autor'),
    url(r'^autores/$', 'apps.autores.views.autores'),
    

  
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
   
    #url(r'^publicaciones/(\d+)/$', 'apps.publicaciones.views.publicacion'),
    

)

handler404 = 'ui.views.error_404'