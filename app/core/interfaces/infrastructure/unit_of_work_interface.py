from typing import Protocol


class IUnitOfWork(Protocol):
    """Интерфейс UnitOfWork."""

    async def commit(self) -> None:
        """Подтвердить транзакцию."""
        raise NotImplementedError

    async def rollback(self) -> None:
        """Откатить транзакцию."""
        raise NotImplementedError

    async def __aenter__(self) -> "IUnitOfWork":
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError
