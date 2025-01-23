class BaseError(Exception):
    """Base class for all application errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
