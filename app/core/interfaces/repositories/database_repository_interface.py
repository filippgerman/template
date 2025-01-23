from abc import abstractmethod
from typing import Protocol


class IDatabaseRepository(Protocol):
    """Interface for database repository."""

    @abstractmethod
    async def check_connection(self) -> bool:
        """Check the database connection."""
        pass
