from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #for static handler
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portal.views.depan', name='depan'),
    url(r'^daftar/$', 'portal.views.daftar', name="daftar"),
    url(r'^jadwal/$', 'portal.views.Jadwal', name="jadwal"),
    url(r'^lokasi/$', 'portal.views.Lokasi', name="lokasi"),
    url(r'^gallery/$', 'portal.views.gallery', name="gallery"),    
    url(r'^penginapan/$', 'portal.views.Penginapan', name="penginapan"),    
    url(r'^faq/$', 'portal.views.FaQ', name="faq"),    
    url(r'^sponsor/$', 'portal.views.Sponsor', name="sponsor"),    
    url(r'^hubungi/$', 'portal.views.Hubungi', name="hubungi"),  
    url(r'^informasi/$', 'portal.views.Informasi', name="informasi"),  
    # url(r'^ilc/', include('ilc.foo.urls')), #for decloping URL
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^tamong123/', include(admin.site.urls)),

)
handler404 = "portal.views.Status"

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   		
   )
