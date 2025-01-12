from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator

from ..async_session.interface import IAsyncSession


class IDatabaseConnector(ABC):
    """Interface for database connector."""

    @abstractmethod
    async def init(self) -> None:
        """Initialize the database connection."""
        ...

    @abstractmethod
    async def close(self) -> None:
        """Close the database connection."""
        ...

    @abstractmethod
    def get_session(self) -> AsyncGenerator[IAsyncSession, None]:
        """Get a database session.

        Returns:
            AsyncGenerator[IAsyncSession, None]: Session generator.

        """
        ...
