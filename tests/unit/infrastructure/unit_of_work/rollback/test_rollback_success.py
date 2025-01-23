from unittest.mock import AsyncMock

import pytest

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.mark.asyncio
async def test_rollback_success(unit_of_work: UnitOfWork, mock_session: AsyncMock) -> None:
    """
    Test the `rollback` method of `UnitOfWork` for a successful rollback.

    This test verifies that the `rollback` method calls the session's `rollback` method.

    Steps:
    1. Arrange: Set up the UnitOfWork with a mocked session.
    2. Act: Call the `rollback` method.
    3. Assert: Verify that the session's `rollback` method was called once.
    """
    # Act
    await unit_of_work.rollback()

    # Assert
    mock_session.rollback.assert_awaited_once()
