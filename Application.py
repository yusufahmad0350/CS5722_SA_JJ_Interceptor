class Application:
    #Model the Application's weather data station with three states: Initialize, Read weather data, and storing the weather data
    def __init__(self):
        self.state = "Initializing"
        self.weather_data = {"temperature": 0.0, "humidity": 0.0, "pressure": 0.0}
    
    def read_data(self):
        self.state = "Reading data from the weather data system"
        #print(self.state)
        # simulate reading data from sensors
        #self.weather_data = {"temperature": 50.0, "humidity": 90.0, "pressure": 980.0}

    def store_data(self):
        self.state = "Storing the data"
        #print(self.state)
        # simulate storing data in a database
        print("Storing weather data:", self.weather_data)