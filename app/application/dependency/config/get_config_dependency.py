from app.config.app import AppConfig


def get_config_dependency() -> AppConfig:
    """
    Provide application configuration.

    Returns:
        AppConfig: Application configuration instance.
    """
    return AppConfig()
