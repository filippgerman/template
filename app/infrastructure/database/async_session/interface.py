from abc import ABC, abstractmethod
from types import TracebackType
from typing import TypeVar, Union

from sqlalchemy.sql import Delete, Insert, Select, Update

QueryType = Union[Select, Insert, Update, Delete]
ResultType = TypeVar("ResultType")


class IAsyncSession(ABC):
    """Abstract interface for database session operations."""

    @abstractmethod
    async def execute(self, query: QueryType) -> ResultType:
        """Execute a database query.

        Args:
            query: The SQLAlchemy query to execute.

        Returns:
            The query result.

        """
        ...

    @abstractmethod
    async def commit(self) -> None:
        """Commit the current transaction."""
        ...

    @abstractmethod
    async def rollback(self) -> None:
        """Rollback the current transaction."""
        ...

    @abstractmethod
    async def close(self) -> None:
        """Close the session."""
        ...

    @abstractmethod
    async def __aenter__(self) -> "IAsyncSession":
        """Enter the async context."""
        ...

    @abstractmethod
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit the async context."""
        ...
