from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings

from app.config.database import DatabaseConfig
from app.config.environment_enum import EnvironmentEnum


class AppConfig(BaseSettings, DatabaseConfig):
    """Configuration settings for the FastAPI application.

    Attributes:
        PROJECT_NAME (str): The name of the project.
        APP_HOST (str): The host address for the application.
        APP_PORT (str): The port number for the application.
        LOG_LEVEL (str): The logging level for the application.
        DEBUG (bool): Flag indicating if debug mode is enabled.
        ENVIRONMENT (EnvironmentEnum): The environment in which the application is running.

    """

    PROJECT_NAME: str = Field(..., env="PROJECT_NAME")
    APP_VERSION: str = Field(..., env="APP_VERSION")
    APP_HOST: str = Field(..., env="APP_HOST")
    APP_PORT: str = Field(..., env="APP_PORT")
    LOG_LEVEL: str = Field(..., env="LOG_LEVEL")
    DEBUG: bool = Field(..., env="DEBUG")
    ENVIRONMENT: EnvironmentEnum = Field(..., env="ENVIRONMENT")

    class Config:
        """Configuration for Pydantic settings.

        Attributes:
            env_file (str): Path to the environment variables file.
            case_sensitive (bool): Flag for case sensitivity.

        """

        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_config() -> AppConfig:
    """Return the application configuration loaded from environment variables.

    Returns:
        AppConfig: The application configuration instance.

    """
    return AppConfig()
