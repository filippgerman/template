from unittest.mock import AsyncMock

import pytest

from app.data_access.repositories.database_repository import DatabaseRepository


@pytest.mark.asyncio
async def test_check_connection_success(mock_db_session: AsyncMock) -> None:
    """
    Test the `check_connection` method of `DatabaseRepository` for a successful connection.

    This test verifies that the `check_connection` method returns True when the database connection succeeds.

    Steps:
    1. Arrange: Mock the session to simulate a successful query execution.
    2. Act: Call the `check_connection` method.
    3. Assert: Verify that the method returns True.
    """
    # Arrange
    repository = DatabaseRepository(session=mock_db_session)
    mock_db_session.execute = AsyncMock()

    # Act
    result = await repository.check_connection()

    # Assert
    assert result is True
