import pytest


@pytest.mark.asyncio
async def test_health_check_redis_success(test_client, mock_health_check_use_case_redis):
    """
    Test successful Redis health check.

    This test verifies that the `/health/redis` endpoint returns a 200 status code
    and the expected JSON response when the Redis health check succeeds.

    Steps:
    1. Use the `test_client` fixture to send a GET request to `/health/redis`.
    2. Assert that the response status code is 200.
    3. Assert that the response JSON matches the expected result.
    4. Verify that the mocked `execute` method was called exactly once.
    """
    mock_health_check_use_case_redis.execute.return_value = {"status": "healthy"}

    # Act
    response = test_client.get("/health/redis")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    mock_health_check_use_case_redis.execute.assert_called_once()
