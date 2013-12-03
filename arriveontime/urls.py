from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('arriveontime.views',
    # Examples:
    #url(r'^$', 'fltservices.views.basic', name='basic'), 
    url(r'^check-flight/(?P<bookingId>\d+)/(?P<user_flight_number>\w+)','check_flight', name = 'check_flight'),
    url(r'^check-flight/(?P<bookingId>\d+)','check_flight', name = 'check_flight'),
    url(r'^save-flight-number/(?P<bookingId>\d+)/(?P<user_flight_number>\w+)','save_flight_number', name = 'save_flight_number'),
    url(r'^bookings-list/','bookings_list' ,name = 'bookings_list'),
    url(r'^airport-info/','airport_info' ,name = 'airport_info'),
    url(r'^login','applogin', name = 'applogin'),
    url(r'^',TemplateView.as_view(template_name="arriveontime/login.html")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),   
)
