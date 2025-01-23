from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.application.dependency.use_cases.heakth_check import (
    get_health_check_use_case_db,
    get_health_check_use_case_redis,
)
from app.core.errors.database_error import DatabaseNotReachable
from app.core.errors.redis_error import RedisNotReachable
from app.core.use_cases.health_check import HealthCheckUseCase

router = APIRouter(prefix="/health", tags=["Health Checks"])


@router.get(
    "/db",
    summary="Database Health Check",
    description="Checks the availability of the database and returns its status.",
    responses={
        200: {
            "description": "Database is reachable",
            "content": {"application/json": {"example": {"status": "healthy"}}},
        },
        503: {
            "description": "Database is unreachable",
            "content": {"application/json": {"example": {"detail": "Database is unreachable"}}},
        },
    },
)
async def health_check_db(use_case: Annotated[HealthCheckUseCase, Depends(get_health_check_use_case_db)]):
    """Health check endpoint for the database."""
    try:
        return await use_case.execute()
    except DatabaseNotReachable as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.get(
    "/redis",
    summary="Redis Health Check",
    description="Checks the availability of the Redis instance and returns its status.",
    responses={
        200: {
            "description": "Redis is reachable",
            "content": {"application/json": {"example": {"status": "healthy"}}},
        },
        503: {
            "description": "Redis is unreachable",
            "content": {"application/json": {"example": {"detail": "Redis is unreachable"}}},
        },
    },
)
async def health_check_redis(use_case: Annotated[HealthCheckUseCase, Depends(get_health_check_use_case_redis)]):
    """Health check endpoint for Redis."""
    try:
        return await use_case.execute()
    except RedisNotReachable as e:
        raise HTTPException(status_code=503, detail=str(e))
