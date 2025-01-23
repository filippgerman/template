from app.core.errors.database_error import DatabaseNotReachable
from app.core.interfaces.repositories.database_repository_interface import IDatabaseRepository


class DatabaseHealthCheckService:
    def __init__(self, repository: IDatabaseRepository):
        self.repository = repository

    async def check_health(self) -> dict:
        is_healthy = await self.repository.check_connection()
        if is_healthy:
            return {"status": "healthy"}
        else:
            raise DatabaseNotReachable("Database is not reachable")
