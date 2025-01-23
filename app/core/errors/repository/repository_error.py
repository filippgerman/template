from app.core.errors.base_error import BaseError


class RepositoryError(BaseError):
    """Base class for repository-related errors."""

    def __init__(self, message: str = "An error occurred in the repository"):
        super().__init__(message)
