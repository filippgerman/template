from pydantic import BaseModel, Field


class RedisConfig(BaseModel):
    """Configuration settings for Redis."""

    REDIS_HOST: str = Field(..., json_schema_extra={"env": "REDIS_HOST"})
    REDIS_PORT: int = Field(..., json_schema_extra={"env": "REDIS_PORT"})
    REDIS_DB: int = Field(..., json_schema_extra={"env": "REDIS_DB"})
    CACHE_TTL: int = Field(..., json_schema_extra={"env": "CACHE_TTL"})
