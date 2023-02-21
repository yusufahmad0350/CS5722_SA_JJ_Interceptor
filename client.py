from application import Application
from concrete_interceptors import LoggingInterceptor, WarningInterceptor
from context import WeatherDataContext
from dispatcher import WeatherDataInterceptorsDispatcher
from interceptor_factory import InterceptorFactory


weather_data_system = Application()
interceptors_dispatcher = WeatherDataInterceptorsDispatcher()

#Entered weather data from sensor
weather_data = {"temperature": 4.7, "humidity": 60.4, "pressure": 1027.5}
weather_data_system.weather_data = weather_data

#Register Interceptors with Dispatcher
logging_interceptor = InterceptorFactory.create_interceptor("logging")
warning_interceptor = InterceptorFactory.create_interceptor("warning")
interceptors_dispatcher.register_reader_interceptor(logging_interceptor)
interceptors_dispatcher.register_writer_interceptor(warning_interceptor)

#Dispatcher to dispatch Interception points
interceptors_dispatcher.dispatch_before_read()
weather_data_system.read_data()
context = WeatherDataContext(weather_data_system)
interceptors_dispatcher.dispatch_after_write(context)
weather_data_system.store_data()