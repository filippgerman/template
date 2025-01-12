from app.core.errors.redis_error import RedisNotReachable
from app.infrastructure.cache.redis_connector import RedisConnector


class RedisHealthCheckService:
    def __init__(self, redis_connector: RedisConnector):
        self.redis_connector = redis_connector

    async def check_health(self) -> dict:
        if not self.redis_connector:
            raise RedisNotReachable("Redis connector is not configured")

        try:
            await self.redis_connector.set("health_check", "ok")
            value = await self.redis_connector.get("health_check")
            if value == "ok":
                return {"status": "healthy"}
            else:
                raise RedisNotReachable("Redis is not reachable")
        except Exception:
            raise RedisNotReachable("Redis is not reachable")
