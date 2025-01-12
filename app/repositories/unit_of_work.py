from app.core.interfaces.repositories.unit_of_work_interface import IUnitOfWork
from app.repositories.database_repository import DatabaseRepository


class UnitOfWork(IUnitOfWork):
    """Implementation of Unit of Work pattern."""

    def __init__(self, session_factory):
        self.session_factory = session_factory
        self.session = None
        self.database_repository = None

    async def __aenter__(self):
        self.session = self.session_factory()
        self.database_repository = DatabaseRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        """Commit the transaction."""
        await self.session.commit()

    async def rollback(self):
        """Rollback the transaction."""
        await self.session.rollback()
