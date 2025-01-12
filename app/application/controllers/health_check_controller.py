from fastapi import APIRouter, Depends, HTTPException

from app.application.dependency.db_dependency import get_db_session
from app.application.dependency.redis_dependency import get_redis_connector
from app.core.errors.database_error import DatabaseNotReachable
from app.core.errors.redis_error import RedisNotReachable
from app.core.use_cases.health_check import HealthCheckUseCase
from app.repositories.unit_of_work import UnitOfWork
from app.services.database_health_check_service import DatabaseHealthCheckService
from app.services.redis_health_check_service import RedisHealthCheckService

router = APIRouter()


@router.get("/health/db")
async def health_check_db(db_session=Depends(get_db_session)):
    """Health check endpoint for the database."""
    uow = UnitOfWork(lambda: db_session)
    service = DatabaseHealthCheckService(uow)
    use_case = HealthCheckUseCase(service)
    try:
        return await use_case.execute()
    except DatabaseNotReachable as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.get("/health/redis")
async def health_check_redis(redis_connector=Depends(get_redis_connector)):
    """Health check endpoint for Redis."""
    service = RedisHealthCheckService(redis_connector=redis_connector)
    try:
        return await service.check_health()
    except RedisNotReachable as e:
        raise HTTPException(status_code=503, detail=str(e))
