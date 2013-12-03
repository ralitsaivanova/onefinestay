from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
import arriveontime.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'fltservices.views.basic', name='basic'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(arriveontime.urls)),
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
