class BaseInterceptor(object):
    """
    BaseInterceptor provides a base class for HTTP traffic
    interceptors implementations.
    """
    def __init__(self, engine):
        self.patchers = []
        self.engine = engine

    def activate(self):
        """
        Activates the traffic interceptor.
        This method must be implemented by any interceptor.
        """
        raise NotImplemented('not implemented')

    def disable(self):
        """
        Disables the traffic interceptor.
        This method must be implemented by any interceptor.
        """
        raise NotImplemented('not implemented')