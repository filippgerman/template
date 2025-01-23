from typing import Optional

from app.core.errors.cache.cache_error import CacheError
from app.core.interfaces.cache.cache_interface import ICache
from app.infrastructure.cache.redis_connector import RedisConnector


class CacheRepository(ICache):
    """Repository for cache operations.

    This class provides methods to interact with the cache, allowing
    setting, getting, and closing cache connections.

    Attributes:
        redis_connector (RedisConnector): The connector for interacting with Redis.
    """

    def __init__(self, redis_connector: RedisConnector):
        """Initialize CacheRepository with a Redis connector.

        Args:
            redis_connector (RedisConnector): The Redis connector instance.
        """
        self.redis_connector = redis_connector

    async def set(self, key: str, value: str, expire: Optional[int] = None) -> None:
        """Set a value in cache with an optional expiration time.

        Args:
            key (str): The key under which the value is stored.
            value (str): The value to store in the cache.
            expire (Optional[int]): The expiration time in seconds.

        Raises:
            CacheError: If there is an error setting the value in the cache.
        """
        try:
            await self.redis_connector.set(key, value, expire)
        except Exception as e:
            raise CacheError(f"Failed to set cache for key {key}") from e

    async def get(self, key: str) -> Optional[str]:
        """Get a value from cache.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            Optional[str]: The value from the cache, or None if not found.

        Raises:
            CacheError: If there is an error retrieving the value from the cache.
        """
        try:
            return await self.redis_connector.get(key)
        except Exception as e:
            raise CacheError(f"Failed to get cache for key {key}") from e

    async def close(self) -> None:
        """Close the cache connection.

        Raises:
            CacheError: If there is an error closing the cache connection.
        """
        try:
            await self.redis_connector.close()
        except Exception as e:
            raise CacheError("Failed to close cache connection") from e
