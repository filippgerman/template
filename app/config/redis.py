from pydantic import Field


class RedisConfig:
    """Configuration settings for Redis.

    Attributes:
        REDIS_HOST (str): The Redis server address.
        REDIS_PORT (int): The port number for the Redis connection.
    """

    REDIS_HOST: str = Field(..., env="REDIS_HOST")
    REDIS_PORT: int = Field(..., env="REDIS_PORT")
