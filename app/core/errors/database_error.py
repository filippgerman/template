from .base_error import ServiceException


class DatabaseNotReachable(ServiceException):
    """Exception raised when the database is not reachable."""

    pass
