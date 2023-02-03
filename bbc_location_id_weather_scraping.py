# -*- coding: utf-8 -*-
"""
A tutorial to scrape the location ID of any city in BBC Weather. 
This code snippet takes city name as input and it hits the BBC Weahter API with a request for location ID. This location ID is used as input in the next part of the code to scrape weather forecast for the city using this location ID.  
*Web scraping might not be legal always. It is a good idea to check the terms of the website you plan to scrape before proceeding. Also, if your code requests a url from a server multiple times, it is a good practice to either cache your requests, or insert a timed delay between consecutive requests.*
"""

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
