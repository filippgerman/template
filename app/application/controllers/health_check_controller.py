from fastapi import APIRouter, Depends

from app.application.dependency.db_dependency import get_db_session
from app.core.use_cases.health_check import HealthCheckUseCase
from app.repositories.unit_of_work import UnitOfWork
from app.services.health_check_service import HealthCheckService

router = APIRouter()


@router.get("/health/db")
async def health_check_db(db_session=Depends(get_db_session)):
    """Health check endpoint for the database."""
    uow = UnitOfWork(lambda: db_session)
    service = HealthCheckService(uow)
    use_case = HealthCheckUseCase(service)
    return await use_case.execute()
