from interceptors import WeatherDataReaderInterceptor, WeatherDataWriterInterceptor


#Logs the data when data is read and stored
class LoggingInterceptor(WeatherDataReaderInterceptor, WeatherDataWriterInterceptor):
    def read_update(self, context):
        print("Reading weather data...")

    def write_update(self, context):
        print("Weather data stored.")
#Check the data and warn accordingly before storing.
class WarningInterceptor(WeatherDataWriterInterceptor):
    def write_update(self, context):
        weather_data_system = context.weather_data_system
        weather_data = weather_data_system.weather_data
        if weather_data["temperature"] >= 30.0:
            print("WARNING: High temperature detected!")
        elif weather_data["temperature"] <= 5.0:
            print("WARNING: Extremely Low temperature detected!")
        if weather_data["humidity"] >= 60.0:
            print("WARNING: High Humidity detected!")
        if weather_data["pressure"] >= 1025:
            print("WARNING: High pressure detected!")