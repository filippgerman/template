from app.config.app import get_config


async def get_database_config() -> dict:
    """Provide database configuration for dependency injection."""
    config = get_config()
    return {
        "db_user": config.DATABASE_USER,
        "db_password": config.DATABASE_PASSWORD,
        "db_server": config.DATABASE_SERVER,
        "db_port": config.DATABASE_PORT,
        "db_name": config.DATABASE_DB,
        "echo": config.DEBUG,
    }
