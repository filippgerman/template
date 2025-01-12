from abc import ABC, abstractmethod


class IHealthCheck(ABC):
    """Interface for health check implementations."""

    @abstractmethod
    async def check_db_health(self) -> dict:
        """Check the health of a service."""
        ...

    @abstractmethod
    async def check_redis_health(self) -> dict:
        """Check the health of the Redis service."""
        ...
