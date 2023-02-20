#Identified two interception points.
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class WeatherDataReaderInterceptor(ABC):
    #Before data read : Reader Set
    @abstractmethod
    def on_before_read(self, context):
        pass
    #After data Store : Writer Set
class WeatherDataWriterInterceptor(ABC):
    @abstractmethod
    def on_after_write(self, context):
        pass