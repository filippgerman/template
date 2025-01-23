from unittest.mock import AsyncMock

import pytest

from app.core.errors.redis_error import RedisNotReachable
from app.services.health_check.redis_health_check_service import RedisHealthCheckService


@pytest.mark.asyncio
async def test_check_health_unexpected_value(mock_cache: AsyncMock) -> None:
    """
    Test the `check_health` method of `RedisHealthCheckService` for an unexpected Redis value.

    This test verifies that the `check_health` method raises a `RedisNotReachable`
    exception when Redis returns an unexpected value.

    Steps:
    1. Arrange: Mock the Redis connector to return an unexpected value.
    2. Act: Call the `check_health` method.
    3. Assert: Verify that the `RedisNotReachable` exception is raised with the correct message.
    """
    # Arrange
    service = RedisHealthCheckService(redis_connector=mock_cache)
    mock_cache.set = AsyncMock(return_value=None)
    mock_cache.get = AsyncMock(return_value="unexpected")

    # Act & Assert
    with pytest.raises(RedisNotReachable, match="Redis returned unexpected value"):
        await service.check_health()
