from redis.asyncio import Redis  # type: ignore


class RedisConnector:
    """Connector for Redis operations."""

    def __init__(self, host: str, port: int):
        self.redis = Redis(host=host, port=port, decode_responses=True)

    async def set(self, key: str, value: str) -> None:
        """Set a value in Redis."""
        await self.redis.set(key, value)

    async def get(self, key: str) -> str:
        """Get a value from Redis."""
        return await self.redis.get(key)

    async def close(self):
        """Close the connection to the Redis server."""
        await self.redis.close()
