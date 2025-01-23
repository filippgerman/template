from typing import Annotated, AsyncGenerator

from fastapi import Depends

from app.application.dependency.config.get_config_dependency import get_config_dependency
from app.config.app import AppConfig
from app.infrastructure.cache.redis_connector import RedisConnector


async def get_redis_connector_dependency(
    config: Annotated[AppConfig, Depends(get_config_dependency)]
) -> AsyncGenerator[RedisConnector, None]:
    """
    Dependency for creating a Redis connector.

    Args:
        config (AppConfig): Application configuration.

    Returns:
        RedisConnector: Configured Redis connector instance.
    """
    connector = RedisConnector(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB,
    )
    try:
        yield connector
    finally:
        await connector.close()
