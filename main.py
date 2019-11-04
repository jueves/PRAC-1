# -*- coding: utf-8 -*-

from eventscraper import getEvents
from weather import getWeather
from location import getLocation
import datetime
# Load API keys
# This two files must be generated by the user with its own api keys
file_aemet = open("aemet_api_key.txt")
aemet_key = file_aemet.readline()
file_aemet.close()
file_gmaps = open("gmaps_api_key.txt")
gmaps_key = file_gmaps.readline()
file_gmaps.close()

# Dummy dates for testing
dummy_date1 = datetime.date(2019, 11, 4)
dummy_date2 = datetime.date(2019, 11, 6)

lagenda_data = getEvents(dummy_date1, dummy_date2)