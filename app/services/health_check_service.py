from fastapi import HTTPException

from app.core.interfaces.services.health_check_interface import IHealthCheck
from app.repositories.unit_of_work import UnitOfWork


class HealthCheckService(IHealthCheck):
    """Service for checking the health of the database."""

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def check_health(self) -> dict:
        """Check the health of the database."""
        async with self.uow as uow:
            is_healthy = await uow.database_repository.check_connection()
            if is_healthy:
                return {"status": "healthy"}
            else:
                raise HTTPException(status_code=503, detail="Database is not reachable")
