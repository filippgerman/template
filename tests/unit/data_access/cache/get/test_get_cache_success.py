from unittest.mock import AsyncMock

import pytest

from app.data_access.cache.cache_repository import CacheRepository


@pytest.mark.asyncio
async def test_get_cache_success():
    """
    Test the `get` method of `CacheRepository` for successful cache retrieval.

    This test verifies that the `get` method correctly retrieves a value from the cache.
    It mocks the Redis connector to ensure the `get` method returns the expected value.

    Steps:
    1. Arrange: Set up the mock Redis connector to return a value.
    2. Act: Call the `get` method.
    3. Assert: Verify that the returned value matches the expected value.
    """
    # Arrange
    redis_connector = AsyncMock()
    expected_value = "test_value"
    redis_connector.get.return_value = expected_value
    cache_repository = CacheRepository(redis_connector)

    key = "test_key"

    # Act
    value = await cache_repository.get(key)

    # Assert
    assert value == expected_value
    redis_connector.get.assert_called_once_with(key)
