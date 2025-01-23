from unittest.mock import AsyncMock

import pytest

from app.data_access.cache.cache_repository import CacheRepository


@pytest.mark.asyncio
async def test_get_cache_miss():
    """
    Test the `get` method of `CacheRepository` for cache miss.

    This test verifies that the `get` method returns None when the key does not exist in the cache.
    It mocks the Redis connector to return None.

    Steps:
    1. Arrange: Set up the mock Redis connector to return None.
    2. Act: Call the `get` method.
    3. Assert: Verify that the returned value is None.
    """
    # Arrange
    redis_connector = AsyncMock()
    redis_connector.get.return_value = None
    cache_repository = CacheRepository(redis_connector)

    key = "non_existent_key"

    # Act
    value = await cache_repository.get(key)

    # Assert
    assert value is None
    redis_connector.get.assert_called_once_with(key)
