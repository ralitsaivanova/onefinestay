from django.conf import settings

import urllib2
import json
from datetime import datetime

class FltStats(object):
        """wrapper for FltStats api"""

        _url = 'https://api.flightstats.com/flex'
        _auth = ''
        
        _auth_get = ''
        
        def __init__(self, *params):
            super(FltStats, self).__init__()
            self._auth = "appId="+params[0]+"&appKey="+params[1]

        def getDelayAptIndex(self,apts):
            url = self._url + "/delayindex/rest/v1/json/airports/"+",".join(apts)+"?"+self._auth+""
            apts = []
            try:    
                response = urllib2.urlopen(url)
                read = response.read()

                dictResponse =    json.loads(read)

                if 'error' not in dictResponse.keys():
                    delayIndexes = dictResponse["delayIndexes"]
                    
                    for item in delayIndexes:
                        apts.append({
                            "name":item["airport"]["name"],
                            "iataCode":item["airport"]["iata"],
                            "city":item["airport"]["city"],
                            "cityCode":item["airport"]["cityCode"],
                            "country":item["airport"]["countryName"],
                            "countryCode":item["airport"]["countryCode"],
                            "normalizedScore":item["normalizedScore"],
                            "flights":item["flights"],
                            "canceled":item["canceled"],
                            "onTime":item["onTime"],
                            "delayed15":item["delayed15"],
                            "delayed30":item["delayed30"],
                            "delayed45":item["delayed45"],
                            })
                    return apts
            except:
                return apts
                
        def getFlightArrival(self,carrier,number,year,month,day):
            url = self._url + "/flightstatus/rest/v2/json/flight/status/"+str(carrier)+"/"+str(number)+"/arr/"+str(year)+"/"+str(month)+"/"+str(day)+"?"+self._auth
            flightStatus = []
            
            try:    
                response = urllib2.urlopen(url)
                read = response.read()
                dictResponse =    json.loads(read)

                if 'error' not in dictResponse.keys():
                    airports = dictResponse["appendix"]["airports"]
                    flightStatuses = dictResponse["flightStatuses"]
                    airport_decode = dict()
                    for item in airports:
                        airport_decode[item["iata"]] = item["name"]+", "+item["city"]+", "+item["countryName"]

                    for item in flightStatuses:
                        flightStatus.append({
                            "carrierCode":item["carrierFsCode"],
                            "flightNumber":item["flightNumber"],
                            "departureApt":airport_decode[item["departureAirportFsCode"]],
                            "arrivalApt":airport_decode[item["arrivalAirportFsCode"]],
                            "departureDate":datetime.strptime(item["operationalTimes"]["publishedDeparture"]["dateLocal"],'%Y-%m-%dT%H:%M:%S.000'),
                            "arrivalDate":datetime.strptime(item["operationalTimes"]["publishedArrival"]["dateLocal"],'%Y-%m-%dT%H:%M:%S.000'),
                        })
                return flightStatus    
            except:
                return flightStatus    




        def getAllAptFlights(self,aptCode,year,month,day,hourOfDay):
            url = self._url + "/schedules/rest/v1/json/to/"+str(aptCode)+"/arriving/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+str(hourOfDay)+"?"+self._auth
            
            flights = []
            try:
                response = urllib2.urlopen(url)
                read = response.read()
                dictResponse =    json.loads(read)
                if 'error' not in dictResponse.keys():
                    airports = dictResponse["appendix"]["airports"]
                    airport_decode = dict()
                    for item in airports:
                        airport_decode[item["iata"]] = item["name"]+", "+item["city"]+", "+item["countryName"]

                    scheduledFlights = dictResponse["scheduledFlights"]
                    for item in scheduledFlights:
                        flights.append({
                                "carrierFsCodeode":item["carrierFsCode"],
                                "flightNumber":item["flightNumber"],
                                "departureApt":airport_decode[item["departureAirportFsCode"]],
                                "arrivalApt":airport_decode[item["arrivalAirportFsCode"]],
                                "departureDate":datetime.strptime(item["departureTime"],'%Y-%m-%dT%H:%M:%S.000'),
                                "arrivalDate":datetime.strptime(item["arrivalTime"],'%Y-%m-%dT%H:%M:%S.000'),
                        })

                    return flights
            except:        
                return flights        
            
            
class AirInfo(object):
    '''get initialized provider based on name'''
    @staticmethod
    def factory(type):    
        if type == "fltstats": return FltStats(settings.FLIGHTSTATS_ID,settings.FLIGHTSTATS_KEY)        
        
            