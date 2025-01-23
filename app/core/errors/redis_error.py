from .base_error import BaseError


class RedisNotReachable(BaseError):
    """Exception raised when Redis is not reachable."""

    pass
