class CacheError(Exception):
    """Exception raised for cache-related errors."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
