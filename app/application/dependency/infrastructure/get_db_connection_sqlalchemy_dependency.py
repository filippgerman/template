from typing import Annotated

from fastapi import Depends

from app.application.dependency.config.get_config_dependency import get_config_dependency
from app.config.app import AppConfig
from app.infrastructure.database.connector.connection import SQLAlchemyConnector
from app.infrastructure.database.connector.interface import IDatabaseConnector


async def get_db_connection_sqlalchemy_dependency(
    config: Annotated[AppConfig, Depends(get_config_dependency)]
) -> IDatabaseConnector:
    """Provide a database connector for dependency injection."""
    return SQLAlchemyConnector(
        db_user=config.DATABASE_USER,
        db_password=config.DATABASE_PASSWORD,
        db_server=config.DATABASE_SERVER,
        db_port=config.DATABASE_PORT,
        db_name=config.DATABASE_DB,
        echo=config.DATABASE_ECHO,
    )
