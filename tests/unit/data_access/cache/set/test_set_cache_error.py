from unittest.mock import AsyncMock

import pytest

from app.core.errors.cache.cache_error import CacheError
from app.data_access.cache.cache_repository import CacheRepository


@pytest.mark.asyncio
async def test_set_cache_error():
    """
    Test the `set` method of `CacheRepository` for handling cache errors.

    This test verifies that the `set` method raises a `CacheError`
    when an error occurs during the cache setting process.
    It mocks the Redis connector to simulate an error.

    Steps:
    1. Arrange: Set up the mock Redis connector to raise an exception.
    2. Act & Assert: Call the `set` method and verify that a CacheError is raised.
    """
    # Arrange
    redis_connector = AsyncMock()
    redis_connector.set.side_effect = Exception("Redis error")
    cache_repository = CacheRepository(redis_connector)

    key = "test_key"
    value = "test_value"
    expire = 3600

    # Act & Assert
    with pytest.raises(CacheError, match=f"Failed to set cache for key {key}"):
        await cache_repository.set(key, value, expire)
