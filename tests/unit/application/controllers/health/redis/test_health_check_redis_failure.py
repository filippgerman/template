import pytest

from app.core.errors.redis_error import RedisNotReachable


@pytest.mark.asyncio
async def test_health_check_redis_failure(test_client, mock_health_check_use_case_redis):
    """
    Test Redis health check failure.

    This test verifies that the `/health/redis` endpoint returns a 503 status code
    and the appropriate error message when a RedisNotReachable exception is raised.

    Steps:
    1. Mock the `execute` method of the Redis health check use case to raise a `RedisNotReachable` exception.
    2. Use the `test_client` fixture to send a GET request to `/health/redis`.
    3. Assert that the response status code is 503.
    4. Assert that the response JSON contains the expected error message.
    5. Verify that the mocked `execute` method was called exactly once.
    """
    # Arrange
    mock_health_check_use_case_redis.execute.side_effect = RedisNotReachable("Redis is unreachable")

    # Act
    response = test_client.get("/health/redis")

    # Assert
    assert response.status_code == 503
    assert response.json() == {"detail": "Redis is unreachable"}
    mock_health_check_use_case_redis.execute.assert_called_once()
