from unittest.mock import AsyncMock

import pytest

from app.services.health_check.database_health_check_service import DatabaseHealthCheckService


@pytest.mark.asyncio
async def test_check_health_success(mock_repository: AsyncMock) -> None:
    """
    Test the `check_health` method of `DatabaseHealthCheckService` for a healthy database.

    This test verifies that the `check_health` method returns a status of
    "healthy" when the database connection is successful.

    Steps:
    1. Arrange: Mock the repository to simulate a successful database connection.
    2. Act: Call the `check_health` method.
    3. Assert: Verify that the returned status is {"status": "healthy"}.
    """
    # Arrange
    service = DatabaseHealthCheckService(repository=mock_repository)
    mock_repository.check_connection = AsyncMock(return_value=True)

    # Act
    result = await service.check_health()

    # Assert
    assert result == {"status": "healthy"}
