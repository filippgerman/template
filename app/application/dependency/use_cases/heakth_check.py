from typing import Annotated

from fastapi import Depends
from redis.asyncio import Redis  # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dependency.infrastructure.get_db_session_dependency import get_db_session_dependency
from app.application.dependency.infrastructure.get_redis_connector_dependency import get_redis_connector_dependency
from app.core.use_cases.health_check import HealthCheckUseCase
from app.data_access.repositories.database_repository import DatabaseRepository
from app.services.health_check.database_health_check_service import DatabaseHealthCheckService
from app.services.health_check.redis_health_check_service import RedisHealthCheckService


async def get_health_check_use_case_db(
    db_session: Annotated[AsyncSession, Depends(get_db_session_dependency)],
) -> HealthCheckUseCase:
    repository = DatabaseRepository(session=db_session)
    service = DatabaseHealthCheckService(repository)
    use_case = HealthCheckUseCase(service)
    return use_case


async def get_health_check_use_case_redis(
    redis_connector: Annotated[Redis, Depends(get_redis_connector_dependency)],
) -> HealthCheckUseCase:
    service = RedisHealthCheckService(redis_connector)
    use_case = HealthCheckUseCase(service)
    return use_case
