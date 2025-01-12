from types import TracebackType

from sqlalchemy.ext.asyncio import AsyncSession

from .interface import IAsyncSession, QueryType, ResultType


class SQLAlchemySession(IAsyncSession):
    """SQLAlchemy implementation of async session interface."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def execute(self, query: QueryType) -> ResultType:
        """Execute a SQLAlchemy query.

        Args:
            query: The SQLAlchemy query to execute.

        Returns:
            The query result.

        """
        return await self._session.execute(query)

    async def commit(self) -> None:
        """Commit the current transaction."""
        await self._session.commit()

    async def rollback(self) -> None:
        """Rollback the current transaction."""
        await self._session.rollback()

    async def close(self) -> None:
        """Close the session."""
        await self._session.close()

    async def __aenter__(self) -> "SQLAlchemySession":
        """Enter the context manager."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit the context manager.

        Args:
            exc_type: The exception type.
            exc_val: The exception value.
            exc_tb: The exception traceback.

        """
        await self.close()
