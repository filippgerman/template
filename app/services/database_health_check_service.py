from app.core.errors.database_error import DatabaseNotReachable
from app.repositories.unit_of_work import UnitOfWork


class DatabaseHealthCheckService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def check_health(self) -> dict:
        async with self.uow as uow:
            is_healthy = await uow.database_repository.check_connection()
            if is_healthy:
                return {"status": "healthy"}
            else:
                raise DatabaseNotReachable("Database is not reachable")
