import pytest

from app.core.errors.redis_error import RedisNotReachable
from app.services.health_check.redis_health_check_service import RedisHealthCheckService


@pytest.mark.asyncio
async def test_check_health_missing_connector() -> None:
    """
    Test the `check_health` method of `RedisHealthCheckService` for a missing Redis connector.

    This test verifies that the `check_health` method raises a `RedisNotReachable`
    exception when the Redis connector is not configured.

    Steps:
    1. Arrange: Create a service without a Redis connector.
    2. Act: Call the `check_health` method.
    3. Assert: Verify that the `RedisNotReachable` exception is raised with the correct message.
    """
    # Arrange
    service = RedisHealthCheckService(redis_connector=None)

    # Act & Assert
    with pytest.raises(RedisNotReachable, match="Redis connector is not configured"):
        await service.check_health()
