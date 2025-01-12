from .base_error import ServiceException


class RedisNotReachable(ServiceException):
    """Exception raised when Redis is not reachable."""

    pass
