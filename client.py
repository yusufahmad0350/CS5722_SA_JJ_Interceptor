from weatherStation import WeatherStation
from concrete_interceptors import LoggingInterceptor, WarningInterceptor
from context import WeatherDataContext
from dispatcher import WeatherDataInterceptorsDispatcher
from interceptor_factory import InterceptorFactory

#Create a weather station object
weather_station = WeatherStation()
interceptors_dispatcher = WeatherDataInterceptorsDispatcher()
#Register Interceptors with Dispatcher
logging_interceptor = InterceptorFactory.create_interceptor("logging")
warning_interceptor = InterceptorFactory.create_interceptor("warning")
interceptors_dispatcher.register_reader_interceptor(logging_interceptor)
interceptors_dispatcher.register_writer_interceptor(warning_interceptor)
interceptors_dispatcher.register_writer_interceptor(logging_interceptor)
weather_station.set_weather_data(temperature=4.7, humidity=90.4, pressure=1068.5)
context_obj= WeatherDataContext(weather_station)
interceptors_dispatcher.dispatch_after_write(context_obj)
