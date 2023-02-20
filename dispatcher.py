
from context import WeatherDataContext

#Used Observer pattern to register the interceptor and dispatch the interceptor 
class WeatherDataInterceptorsDispatcher:
    def __init__(self):
        self.reader_interceptors = []
        self.writer_interceptors = []

    def register_reader_interceptor(self, interceptor):
        self.reader_interceptors.append(interceptor)

    def remove_reader_interceptor(self, interceptor):
        self.reader_interceptors.remove(interceptor)

    def register_writer_interceptor(self, interceptor):
        self.writer_interceptors.append(interceptor)

    def remove_writer_interceptor(self, interceptor):
        self.writer_interceptors.remove(interceptor)

    def dispatch_before_read(self):
        context = WeatherDataContext(self)
        for interceptor in self.reader_interceptors:
            interceptor.on_before_read(context)

    def dispatch_after_write(self, context):
        for interceptor in self.writer_interceptors:
            interceptor.on_after_write(context)