# -*- coding: utf-8 -*-
"""
Scraping using Geocoding API of Open Street Maps (OSM)
We would be using the Nominatim API to scrape geocoding information of any open ended address text using Python.
"""

# no need to install these if using Google Colab
# !pip install geopandas
# !pip install geopy

#import nominatim api
from geopy.geocoders import Nominatim

#activate nominatim geocoder
locator = Nominatim(user_agent="myGeocoder")
#type any address text
location = locator.geocode("Ceres")

#print lattitude and longitude of the address
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

#the API output has multiple other details as a json like altitude, lattitude, longitude, correct raw addres, etc.
#printing all the informaton
location.raw,location.point,location.longitude,location.latitude,location.altitude,location.address

#trying another address
location2 = locator.geocode("IIT Madras")

#printing all the informaton
location2.raw,location2.point,location2.longitude,location2.latitude,location2.altitude,location2.address





