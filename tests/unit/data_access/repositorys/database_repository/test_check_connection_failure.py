from unittest.mock import AsyncMock

import pytest
from sqlalchemy.exc import SQLAlchemyError

from app.data_access.repositories.database_repository import DatabaseRepository


@pytest.mark.asyncio
async def test_check_connection_failure(mock_db_session: AsyncMock) -> None:
    """
    Test the `check_connection` method of `DatabaseRepository` for a failed connection.

    This test verifies that the `check_connection` method returns False
    when the database connection fails due to an exception.

    Steps:
    1. Arrange: Mock the session to raise an SQLAlchemyError during query execution.
    2. Act: Call the `check_connection` method.
    3. Assert: Verify that the method returns False.
    """
    # Arrange
    repository = DatabaseRepository(session=mock_db_session)
    mock_db_session.execute = AsyncMock(side_effect=SQLAlchemyError)

    # Act
    result = await repository.check_connection()

    # Assert
    assert result is False
