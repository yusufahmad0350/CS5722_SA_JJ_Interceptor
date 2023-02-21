from concrete_interceptors import LoggingInterceptor, WarningInterceptor
class InterceptorFactory:
    @staticmethod
    def create_interceptor(interceptor_type):
        if interceptor_type == "logging":
            return LoggingInterceptor()
        elif interceptor_type == "warning":
            return WarningInterceptor()
        else:
            raise ValueError("Invalid interceptor type")