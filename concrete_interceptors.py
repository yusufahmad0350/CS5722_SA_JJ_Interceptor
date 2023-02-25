from context import WeatherDataContext
from interceptors import WeatherDataReaderInterceptor, WeatherDataWriterInterceptor
from abc import ABC, abstractmethod
import logging

#Logs the data when data is read and stored
class LoggingInterceptor(WeatherDataReaderInterceptor, WeatherDataWriterInterceptor):
    def read_update(self, context):
       
        logging.basicConfig(filename='weatherRead.log', level=logging.DEBUG)
        logging.info("Reading weather data...")
        
   
    def write_update(self, context):
        weather_station= context.get_weather_station()
        weather_data = weather_station.get_weather_data()
        logging.basicConfig(filename='weatherWrite.log', level=logging.DEBUG)
        logging.info("Weather data stored.")
        logging.info(weather_data["temperature"])
        
    
        
    
#Check the data and warn accordingly before storing.
class WarningInterceptor(WeatherDataWriterInterceptor):
    def write_update(self, context):
        
        weather_station= context.get_weather_station()
        weather_data = weather_station.get_weather_data()
        if weather_data["temperature"] >= 30.0:
            
            print("WARNING: High temperature detected!")
        elif weather_data["temperature"] <= 5.0:
            print("WARNING: Extremely Low temperature detected!")
        if weather_data["humidity"] >= 60.0:
            print("WARNING: High Humidity detected!")
        if weather_data["pressure"] >= 1025:
            print("WARNING: High pressure detected!")
            
