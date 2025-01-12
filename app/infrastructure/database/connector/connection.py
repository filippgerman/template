import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.database.async_session.interface import IAsyncSession
from app.infrastructure.database.async_session.sqlalchemy import SQLAlchemySession
from app.infrastructure.database.connector.interface import IDatabaseConnector


class SQLAlchemyConnector(IDatabaseConnector):
    """PostgreSQL database connector implementation.

    Attributes:
        engine (AsyncEngine): The SQLAlchemy engine for asynchronous database operations.
        session_factory (sessionmaker): Factory for creating new database sessions.
        logger (logging.Logger): Logger for logging database operations.

    Methods:
        _construct_database_url: Constructs the database URL from provided parameters.
        init: Initializes the database connection.
        close: Closes the database connection.
        get_session: Returns a new database session.

    """

    def __init__(
        self,
        db_user: str,
        db_password: str,
        db_server: str,
        db_port: str,
        db_name: str,
        *,
        echo: bool = False,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            self._construct_database_url(db_user, db_password, db_server, db_port, db_name),
            echo=echo,
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        self.logger = logging.getLogger(__name__)

    def _construct_database_url(
        self,
        db_user: str,
        db_password: str,
        db_server: str,
        db_port: str,
        db_name: str,
    ) -> str:
        """Construct the database URL from provided parameters.

        Args:
            db_user (str): The database user.
            db_password (str): The database password.
            db_server (str): The database server address.
            db_port (str): The database port.
            db_name (str): The database name.

        Returns:
            str: The constructed database URL.

        """
        return f"postgresql+asyncpg://{db_user}:{db_password}" f"@{db_server}:{db_port}/{db_name}"

    async def init(self) -> None:
        """Initialize the database connection."""
        self.logger.info("Database connection initialized.")

    async def close(self) -> None:
        """Close the database connection."""
        self.logger.info("Closing database connection.")
        await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[IAsyncSession, None]:
        """Get a database session."""
        session = self.session_factory()
        async with session as sess:
            yield SQLAlchemySession(sess)
