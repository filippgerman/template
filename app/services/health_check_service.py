from typing import Optional

from app.core.errors.database_error import DatabaseNotReachable
from app.core.errors.redis_error import RedisNotReachable
from app.core.interfaces.services.health_check_interface import IHealthCheck
from app.infrastructure.cache.redis_connector import RedisConnector
from app.repositories.unit_of_work import UnitOfWork


class HealthCheckService(IHealthCheck):
    """Service for checking the health of the database and Redis."""

    def __init__(self, uow: UnitOfWork, redis_connector: Optional[RedisConnector] = None):
        self.uow = uow
        self.redis_connector = redis_connector

    async def check_db_health(self) -> dict:
        """Check the health of the database."""
        async with self.uow as uow:
            is_healthy = await uow.database_repository.check_connection()
            if is_healthy:
                return {"status": "healthy"}
            else:
                raise DatabaseNotReachable("Database is not reachable")

    async def check_redis_health(self) -> dict:
        """Check the health of the Redis service."""
        if not self.redis_connector:
            raise RedisNotReachable("Redis connector is not configured")

        try:
            await self.redis_connector.set("health_check", "ok")
            value = await self.redis_connector.get("health_check")
            if value == "ok":
                return {"status": "healthy"}
            else:
                raise RedisNotReachable("Redis is not reachable")
        except Exception:
            raise RedisNotReachable("Redis is not reachable")
