from unittest.mock import AsyncMock

import pytest

from app.core.errors.database_error import DatabaseNotReachable
from app.services.health_check.database_health_check_service import DatabaseHealthCheckService


@pytest.mark.asyncio
async def test_check_health_failure(mock_repository: AsyncMock) -> None:
    """
    Test the `check_health` method of `DatabaseHealthCheckService` for an unreachable database.

    This test verifies that the `check_health` method raises a `DatabaseNotReachable`
    exception when the database connection fails.

    Steps:
    1. Arrange: Mock the repository to simulate a failed database connection.
    2. Act: Call the `check_health` method.
    3. Assert: Verify that the `DatabaseNotReachable` exception is raised with the correct message.
    """
    # Arrange
    service = DatabaseHealthCheckService(repository=mock_repository)
    mock_repository.check_connection = AsyncMock(return_value=False)

    # Act & Assert
    with pytest.raises(DatabaseNotReachable, match="Database is not reachable"):
        await service.check_health()
