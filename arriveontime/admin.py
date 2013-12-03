from django.contrib import admin
from models import Booking, Airport, City

class BookingAdmin(admin.ModelAdmin):
    list_display = ( 'reference','date_from','city','flight_number')
    date_hierarchy = 'date_from'

admin.site.register(Booking, BookingAdmin)

class AirportAdmin(admin.ModelAdmin):
	list_display = ( 'code','city',)
admin.site.register(Airport, AirportAdmin)

class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'country','code')
admin.site.register(City, CityAdmin)

