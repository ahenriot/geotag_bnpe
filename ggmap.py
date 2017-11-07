# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------------
# @BRGM - 2017
# A.HENRIOT
# script python (2.7 ou 3) qui vise à géocoder des points
# le script utilise le paquet googlemaps et une api_key perso (abel)
#----------------------------------------------------------------------------------------------
import googlemaps
from datetime import datetime
import requests

api_key='AIzaSyCpUfmd0TyvH0_LlJKMXObzfxWwp1r1gls'
gmaps = googlemaps.Client(key=api_key)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Test avec request
requests.get('https://google.com', verify=True)
requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=%s' % api_key)