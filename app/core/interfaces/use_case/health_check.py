from typing import Protocol


class IHealthCheckUseCase(Protocol):
    """Interface for health check use case."""

    async def execute(self) -> dict:
        """Execute the health check."""
        raise NotImplementedError("This method should be implemented by a subclass")
