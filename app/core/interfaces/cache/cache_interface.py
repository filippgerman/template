from abc import ABC, abstractmethod
from typing import Optional


class ICache(ABC):
    """Interface for cache operations."""

    @abstractmethod
    async def set(self, key: str, value: str, expire: Optional[int] = None) -> None:
        """Set a value in cache with an optional expiration time."""
        ...

    @abstractmethod
    async def get(self, key: str) -> Optional[str]:
        """Get a value from cache."""
        ...

    @abstractmethod
    async def close(self) -> None:
        """Close the cache connection."""
        ...
