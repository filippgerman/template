from abc import ABC, abstractmethod


class IUnitOfWork(ABC):
    """Interface for Unit of Work pattern."""

    @abstractmethod
    async def __aenter__(self):
        """Enter the runtime context related to this object."""
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the runtime context related to this object."""
        ...

    @abstractmethod
    async def commit(self):
        """Commit the transaction."""
        ...

    @abstractmethod
    async def rollback(self):
        """Rollback the transaction."""
        ...
