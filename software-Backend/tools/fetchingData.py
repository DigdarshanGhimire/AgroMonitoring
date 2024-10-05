import openmeteo_requests
import requests_cache
from retry_requests import retry
import datetime
import pandas as pd
import math



class Retriever:
	def __init__(self,latitude,longitude) -> None:
		self.cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
		self.retry_session = retry(self.cache_session, retries = 5, backoff_factor = 0.2)
		self.openmeteo = openmeteo_requests.Client(session = self.retry_session)
		self.coordinates = (latitude,longitude)
		self.url = "https://api.open-meteo.com/v1/forecast"
		self.params = {
			"latitude": latitude,
			"longitude": longitude,
			"current": ["temperature_2m", "relative_humidity_2m", "precipitation", "direct_radiation_instant"],
			"hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "soil_moisture_27_to_81cm", "direct_radiation_instant", 'evapotranspiration'],
			"timezone":"Asia/Kathmandu"
		}
  
	
	def getResponses(self):
		self.responses = self.openmeteo.weather_api(self.url, params=self.params)
		self.response = self.responses[0]
		self.current = self.response.Current()
		self.hourly = self.response.Hourly()
		self.stats = [[], [], [], [], [], []]

		for i in range(6):
			for j in range(24):
				self.stats[i].append(self.hourly.Variables(i).Values(j))
    
	def average(self):
		self.averages = []
		for factor in self.stats:
			average = sum(factor)/len(factor)
			self.averages.append(average)
   
	def currentData(self):
		self.temperature = self.current.Variables(0).Value()
		self.humidity = self.current.Variables(1).Value()
		self.precipitation = self.current.Variables(2).Value()
		self.solarRadiation = self.current.Variables(3).Value()
  




 


if __name__ == "__main__":
	retriever = Retriever(26.7891,86.732)
	


    





