from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class DatabaseRepository:
    """Repository for database operations."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def check_connection(self) -> bool:
        """Check the database connection."""
        try:
            await self.session.execute(text("SELECT 1"))
            return True
        except SQLAlchemyError:
            return False
