from unittest.mock import AsyncMock

import pytest

from app.core.errors.redis_error import RedisNotReachable
from app.services.health_check.redis_health_check_service import RedisHealthCheckService


@pytest.mark.asyncio
async def test_check_health_redis_unreachable(mock_cache: AsyncMock) -> None:
    """
    Test the `check_health` method of `RedisHealthCheckService` for an unreachable Redis.

    This test verifies that the `check_health` method raises a `RedisNotReachable`
    exception when an exception occurs while interacting with Redis.

    Steps:
    1. Arrange: Mock the Redis connector to raise an exception during operations.
    2. Act: Call the `check_health` method.
    3. Assert: Verify that the `RedisNotReachable` exception is raised with the correct message.
    """
    # Arrange
    service = RedisHealthCheckService(redis_connector=mock_cache)
    mock_cache.set = AsyncMock(side_effect=Exception("Redis error"))

    # Act & Assert
    with pytest.raises(RedisNotReachable, match="Redis is not reachable"):
        await service.check_health()
