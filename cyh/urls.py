from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyh.views.home', name='home'),
    # url(r'^cyh/', include('cyh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^$', 'inicio.views.inicio'),
   

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^autores/(\d+)/$', 'autores.views.autor'),
    url(r'^autores/lista/$', 'autores.views.lista'),
    url(r'^publicaciones/(\d+)/$', 'publicaciones.views.publicacion'),
    url(r'^publicaciones/lista/$', 'publicaciones.views.lista'),


)
