from sqlalchemy.ext.asyncio import AsyncSession

from app.core.interfaces.infrastructure.unit_of_work_interface import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    """Реализация UnitOfWork."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self) -> None:
        """Подтвердить транзакцию."""
        await self.session.commit()

    async def rollback(self) -> None:
        """Откатить транзакцию."""
        await self.session.rollback()

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
