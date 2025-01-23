from unittest.mock import AsyncMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.fixture
def mock_session() -> AsyncMock:
    """Mock for AsyncSession."""
    return AsyncMock(spec=AsyncSession)


@pytest.fixture
def unit_of_work(mock_session: AsyncMock) -> UnitOfWork:
    """Fixture for UnitOfWork with a mocked session."""
    return UnitOfWork(session=mock_session)
