#Identified two interception points. May considered as PreMarrshallRequest() and PostMarshallRequest()
from abc import ABC, abstractmethod
class WeatherDataReaderInterceptor(ABC):
#Before data read : Reader Set
    @abstractmethod
    def read_update(self, context):
        pass
#After data Store : Writer Set
class WeatherDataWriterInterceptor(ABC):
    @abstractmethod
    def write_update(self, context):
        pass