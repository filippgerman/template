from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends

from app.application.dependency.infrastructure.get_db_connection_sqlalchemy_dependency import (
    get_db_connection_sqlalchemy_dependency,
)
from app.infrastructure.database.async_session.interface import IAsyncSession
from app.infrastructure.database.connector.connection import IDatabaseConnector


async def get_db_session_dependency(
    connector: Annotated[IDatabaseConnector, Depends(get_db_connection_sqlalchemy_dependency)]
) -> AsyncGenerator[IAsyncSession, None]:
    """Provide a database session for dependency injection.

    Args:
        connector (IDatabaseConnector): The database connector.

    Returns:
        AsyncGenerator[IAsyncSession, None]: The database session.
    """
    async for session in connector.get_session():
        yield session
