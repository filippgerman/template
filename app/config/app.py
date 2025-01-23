from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings

from app.config.database import DatabaseConfig
from app.config.environment_enum import EnvironmentEnum
from app.config.redis import RedisConfig
from app.config.sentry_config import SentryConfig


class AppConfig(BaseSettings, DatabaseConfig, RedisConfig, SentryConfig):
    """Configuration settings for the FastAPI application."""

    PROJECT_NAME: str = Field(..., json_schema_extra={"env": "PROJECT_NAME"})
    APP_VERSION: str = Field(..., json_schema_extra={"env": "APP_VERSION"})
    APP_HOST: str = Field(..., json_schema_extra={"env": "APP_HOST"})
    APP_PORT: str = Field(..., json_schema_extra={"env": "APP_PORT"})

    LOG_LEVEL: str = Field(..., json_schema_extra={"env": "LOG_LEVEL"})
    DEBUG: bool = Field(..., json_schema_extra={"env": "DEBUG"})
    ENVIRONMENT: EnvironmentEnum = Field(..., json_schema_extra={"env": "ENVIRONMENT"})

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
    }


@lru_cache
def get_config() -> AppConfig:
    """
    Return the application configuration loaded from environment variables.

    Automatically uses an `.env` file based on the current environment.
    """
    return AppConfig()
