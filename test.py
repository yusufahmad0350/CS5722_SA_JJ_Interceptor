from application import Application
from concrete_interceptors import LoggingInterceptor, WarningInterceptor
from dispatcher import WeatherDataInterceptorsDispatcher
from context import WeatherDataContext


weather_data_system = Application()
interceptors_dispatcher = WeatherDataInterceptorsDispatcher()

#Entered weather data from sensor
weather_data = {"temperature": 4.0, "humidity": 60.0, "pressure": 1027.0}
weather_data_system.weather_data = weather_data

#Register Interceptors with Dispatcher
logging_interceptor = LoggingInterceptor()
warning_interceptor = WarningInterceptor()
interceptors_dispatcher.register_reader_interceptor(logging_interceptor)
interceptors_dispatcher.register_writer_interceptor(warning_interceptor)

#Dispatcher to dispatch Interception points
interceptors_dispatcher.dispatch_before_read()
weather_data_system.read_data()
context = WeatherDataContext(weather_data_system)
interceptors_dispatcher.dispatch_after_write(context)
weather_data_system.store_data()