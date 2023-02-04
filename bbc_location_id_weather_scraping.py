import os
import requests               # to get the webpage
import json                   # to convert API to json format

from urllib.parse import urlencode
import numpy as np
import pandas as pd
import re                     # regular expression operators

test_city = "Pittsfield"
location_url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode({
   'api_key': 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
   's': test_city,
   'stack': 'aws',
   'locale': 'en',
   'filter': 'international',
   'place-types': 'settlement,airport,district',
   'order': 'importance',
   'a': 'true',
   'format': 'json'
})
location_url

result = requests.get(location_url).json()
result

# Print location id
result['response']['results']['results'][0]['id']

"""# Creating a function to output location id by taking any city name as input."""

def getlocid(city):
    city = city.lower() # convert city name to lowercase to standardize format
    # Convert into an API call using URL encoding
    location_url = 'https://locator-service.api.bbci.co.uk/locations?' + urlencode({
      'api_key': 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv',
      's': city,
      'stack': 'aws',
      'locale': 'en',
      'filter': 'international',
      'place-types': 'settlement,airport,district',
      'order': 'importance',
      'a': 'true',
      'format': 'json'
    })
    result = requests.get(location_url).json()
    locid = result['response']['results']['results'][0]['id']
    return locid

getlocid('Toronto')

