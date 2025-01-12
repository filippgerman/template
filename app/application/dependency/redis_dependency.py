from collections.abc import AsyncGenerator

from app.config.app import get_config
from app.infrastructure.cache.redis_connector import RedisConnector


async def get_redis_connector() -> AsyncGenerator[RedisConnector, None]:
    """Provide a Redis connector for dependency injection."""
    config = get_config()
    connector = RedisConnector(host=config.REDIS_HOST, port=config.REDIS_PORT)
    await connector.connect()
    try:
        yield connector
    finally:
        await connector.close()
