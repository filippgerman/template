from unittest.mock import AsyncMock

import pytest

from app.data_access.cache.cache_repository import CacheRepository


@pytest.mark.asyncio
async def test_close_cache_success():
    """
    Test the `close` method of `CacheRepository` for successful cache connection closure.

    This test verifies that the `close` method correctly closes the cache connection.
    It mocks the Redis connector to ensure the `close` method is called.

    Steps:
    1. Arrange: Set up the mock Redis connector.
    2. Act: Call the `close` method.
    3. Assert: Verify that the `close` method was called on the Redis connector.
    """
    # Arrange
    redis_connector = AsyncMock()
    cache_repository = CacheRepository(redis_connector)

    # Act
    await cache_repository.close()

    # Assert
    redis_connector.close.assert_called_once()
