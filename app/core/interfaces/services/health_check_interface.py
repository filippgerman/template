from abc import ABC, abstractmethod


class IHealthCheck(ABC):
    """Interface for health check implementations."""

    @abstractmethod
    async def check_health(self) -> dict:
        """Check the health of a service."""
        ...
