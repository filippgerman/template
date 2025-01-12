from app.core.interfaces.services.health_check_interface import IHealthCheck


class HealthCheckUseCase:
    """Use case for health check."""

    def __init__(self, health_checker: IHealthCheck):
        self.health_checker = health_checker

    async def execute(self) -> dict:
        """Execute the health check."""
        return await self.health_checker.check_health()
