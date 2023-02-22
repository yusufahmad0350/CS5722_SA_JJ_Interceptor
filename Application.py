class WeatherStation:
    #Model the Application's weather data station with three states: Initialize, Read weather data, and storing the weather data
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0  
         
    def get_weather_data(self):
        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": self.pressure
        }

    def set_weather_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure