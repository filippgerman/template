from typing import Annotated

from fastapi import Depends

from app.application.dependency.config_dependency import get_database_config
from app.infrastructure.database.connector.connection import SQLAlchemyConnector


async def get_db_connector(config: Annotated[dict, Depends(get_database_config)]) -> SQLAlchemyConnector:
    """Provide a database connector for dependency injection."""
    return SQLAlchemyConnector(
        db_user=config["db_user"],
        db_password=config["db_password"],
        db_server=config["db_server"],
        db_port=config["db_port"],
        db_name=config["db_name"],
        echo=config["echo"],
    )


async def get_db_session(connector: SQLAlchemyConnector = Depends(get_db_connector)):
    """Provide a database session for dependency injection."""
    async for session in connector.get_session():
        yield session
