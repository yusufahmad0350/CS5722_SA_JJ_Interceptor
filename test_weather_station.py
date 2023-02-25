import pytest
from application import WeatherStation
from concrete_interceptors import LoggingInterceptor, WarningInterceptor
from context import WeatherDataContext
from dispatcher import WeatherDataInterceptorsDispatcher
from interceptor_factory import InterceptorFactory

@pytest.fixture
def weather_station():
    return WeatherStation()

@pytest.fixture
def test_interceptor_dispatcher():
    interceptors_dispatcher = WeatherDataInterceptorsDispatcher()
    logging_interceptor = InterceptorFactory.create_interceptor("logging")
    warning_interceptor = InterceptorFactory.create_interceptor("warning")
    interceptors_dispatcher.register_reader_interceptor(logging_interceptor)
    interceptors_dispatcher.register_writer_interceptor(warning_interceptor)
    interceptors_dispatcher.register_writer_interceptor(logging_interceptor)
    return interceptors_dispatcher

def test_weather_station_set_data(weather_station):
    weather_station.set_weather_data(temperature=4.7, humidity=90.4, pressure=1068.5)
    assert weather_station.get_weather_data()["temperature"] == 4.7
    assert weather_station.get_weather_data()["humidity"] == 90.4
    assert weather_station.get_weather_data()["pressure"] == 1068.5

def test_logging_interceptor(weather_station, test_interceptor_dispatcher):
    weather_station.set_weather_data(temperature=4.7, humidity=90.4, pressure=1068.5)
    context_obj= WeatherDataContext(weather_station)
    test_interceptor_dispatcher.dispatch_before_read()
    test_interceptor_dispatcher.dispatch_after_write(context_obj)
    # Verify that the logging interceptor has logged the data
    with open('weatherWrite.log', 'r') as file:
        log_data = file.read()
        assert "Weather data stored." in log_data
        assert "4.7" in log_data

