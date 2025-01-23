from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.dependency.infrastructure.get_db_session_dependency import get_db_session_dependency
from app.core.interfaces.infrastructure.unit_of_work_interface import IUnitOfWork
from app.infrastructure.database.unit_of_work import UnitOfWork


async def get_unit_of_work_dependency(
    session: Annotated[AsyncSession, Depends(get_db_session_dependency)]
) -> IUnitOfWork:
    """Get the unit of work dependency.

    Args:
        session (AsyncSession): The database session.

    Returns:
        IUnitOfWork: The unit of work.
    """
    return UnitOfWork(session)
