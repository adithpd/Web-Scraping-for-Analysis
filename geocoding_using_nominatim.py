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





