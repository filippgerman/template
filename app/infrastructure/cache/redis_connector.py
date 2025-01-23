from typing import Optional

from redis.asyncio import Redis  # type: ignore


class RedisConnector:
    """Connector for Redis operations."""

    def __init__(self, host: str, port: int, db: int):
        self.redis = Redis(host=host, port=port, db=db, decode_responses=True)

    async def set(self, key: str, value: str, expire: Optional[int] = None) -> None:
        """Set a value in Redis with an optional expiration time."""
        await self.redis.set(key, value, ex=expire)

    async def get(self, key: str) -> str:
        """Get a value from Redis."""
        return await self.redis.get(key)

    async def close(self):
        """Close the connection to the Redis server."""
        await self.redis.close()
