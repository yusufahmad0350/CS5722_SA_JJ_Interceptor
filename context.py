class WeatherDataContext:
    def __init__(self, weather_station):
        self.weather_station = weather_station
        
    def get_weather_station(self):
        return self.weather_station