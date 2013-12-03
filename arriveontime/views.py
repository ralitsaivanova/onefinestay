from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from models import Booking,Airport, City

from flyinfo import AirInfo
from django.conf import settings
from models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required



def applogin(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user and user.is_active:
        login(request, user)
        return redirect("bookings-list/")   
    else:
       return redirect("/") 

@login_required(login_url='/')
def bookings_list(request):
    today = datetime.today()
    bookings = request.user.booking_set.filter(date_from__startswith=today.date())
    return render_to_response('arriveontime/list.html',
                          {'bookings':bookings},
                          context_instance=RequestContext(request))
    
@login_required(login_url='/')
def airport_info(request):
    today = datetime.today()
    bookings = request.user.booking_set.filter(date_from__startswith=today.date())
    cities = bookings.values('city').distinct()
    codes = Airport.objects.filter(city__in = cities).values('code')
    codes = [(a["code"]) for a in codes]
    service = AirInfo.factory('fltstats')
    aptsDelay = service.getDelayAptIndex(codes)
    
    return render_to_response('arriveontime/airport_info.html',
                          {'aptsDelay':aptsDelay},
                          context_instance=RequestContext(request))

def check_flight(request,bookingId,user_flight_number=False):
    booking = get_object_or_404(Booking,pk=bookingId)
    date_from = booking.date_from
    if user_flight_number:
        flight_number = user_flight_number
    else:
        flight_number = booking.flight_number
        
    
    service = AirInfo.factory('fltstats')

    flightInfo = service.getFlightArrival(flight_number[0:2],flight_number[2:],date_from.year,date_from.month,date_from.day)

    if len(flightInfo) == 0:
        flightInfo = dict()
        flightInfo["number"] = flight_number
        flightInfo["bookingId"] = bookingId
        return render_to_response('arriveontime/no_flight_info.html',
                          {'flightInfo':flightInfo},
                          context_instance=RequestContext(request))
    else:    
        return render_to_response('arriveontime/check_flight.html',
                          {'flightInfo':flightInfo,'user_flight_number':user_flight_number,"bookingId":bookingId},
                          context_instance=RequestContext(request))

def save_flight_number(request,bookingId,user_flight_number):
    try:
        booking = Booking.objects.get(pk=bookingId)
        booking.flight_number = user_flight_number
        booking.save()
        return HttpResponse('ok')
    except:    
        return HttpResponse('ko')





        '''
def importjson(request):
    import json
    import random
    from django.contrib.auth.models import User


    with open('/home/rali/FlightDetails.json') as data_file:    
        data = json.load(data_file)

    bookings = data["ofsplatform"]["booking_service"]["bookings"]  


    for item in bookings:
        city = City.objects.get(code=item["location"])  
        user = User.objects.get(pk=random.randint(1,5))
        b = Booking(reference=item["reference"],date_from = item["date_from"],city = city,flight_number = item["flight_number"])
        b.save()    
        b.users.add(user) 

        
    assert False, data
    '''