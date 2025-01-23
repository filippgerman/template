from unittest.mock import AsyncMock

import pytest

from app.core.errors.cache.cache_error import CacheError
from app.data_access.cache.cache_repository import CacheRepository


@pytest.mark.asyncio
async def test_close_cache_error():
    """
    Test the `close` method of `CacheRepository` for handling cache connection errors.

    This test verifies that the `close` method raises a `CacheError`
    when an error occurs during the cache connection closure process.
    It mocks the Redis connector to simulate an error.

    Steps:
    1. Arrange: Set up the mock Redis connector to raise an exception.
    2. Act & Assert: Call the `close` method and verify that a CacheError is raised.
    """
    # Arrange
    redis_connector = AsyncMock()
    redis_connector.close.side_effect = Exception("Redis error")
    cache_repository = CacheRepository(redis_connector)

    # Act & Assert
    with pytest.raises(CacheError, match="Failed to close cache connection"):
        await cache_repository.close()
