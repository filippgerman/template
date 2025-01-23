from typing import Annotated

from fastapi import Depends

from app.application.dependency.infrastructure.get_redis_connector_dependency import get_redis_connector_dependency
from app.core.interfaces.cache.cache_interface import ICache
from app.data_access.cache.cache_repository import CacheRepository
from app.infrastructure.cache.redis_connector import RedisConnector


async def get_cache_repository_dependency(
    redis_connector: Annotated[RedisConnector, Depends(get_redis_connector_dependency)],
) -> ICache:
    """Get the cache repository dependency.

    Args:
        redis_connector (RedisConnector): The Redis connector.

    Returns:
        ICache: The cache repository.
    """
    return CacheRepository(redis_connector)
