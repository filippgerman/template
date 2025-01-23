from unittest.mock import AsyncMock

import pytest

from app.data_access.cache.cache_repository import CacheRepository


@pytest.mark.asyncio
async def test_set_cache_success():
    """
    Test the `set` method of `CacheRepository` for successful cache setting.

    This test verifies that the `set` method correctly sets a value in the cache.
    It mocks the Redis connector to ensure the `set` method is called with the correct arguments.

    Steps:
    1. Arrange: Set up the mock Redis connector.
    2. Act: Call the `set` method.
    3. Assert: Verify that the `set` method was called on the Redis connector.
    """
    # Arrange
    redis_connector = AsyncMock()
    cache_repository = CacheRepository(redis_connector)

    key = "test_key"
    value = "test_value"
    expire = 3600

    # Act
    await cache_repository.set(key, value, expire)

    # Assert
    redis_connector.set.assert_called_once_with(key, value, expire)
