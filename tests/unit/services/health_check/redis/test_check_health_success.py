from unittest.mock import AsyncMock

import pytest

from app.services.health_check.redis_health_check_service import RedisHealthCheckService


@pytest.mark.asyncio
async def test_check_health_success(mock_cache: AsyncMock) -> None:
    """
    Test the `check_health` method of `RedisHealthCheckService` for a healthy Redis.

    This test verifies that the `check_health` method returns a status of "healthy"
    when Redis is reachable and returns the expected value.

    Steps:
    1. Arrange: Mock the Redis connector to simulate successful operations.
    2. Act: Call the `check_health` method.
    3. Assert: Verify that the returned status is {"status": "healthy"}.
    """
    # Arrange
    service = RedisHealthCheckService(redis_connector=mock_cache)
    mock_cache.set = AsyncMock(return_value=None)
    mock_cache.get = AsyncMock(return_value="ok")

    # Act
    result = await service.check_health()

    # Assert
    assert result == {"status": "healthy"}
