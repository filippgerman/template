from unittest.mock import AsyncMock

import pytest

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.mark.asyncio
async def test_aexit_calls_commit_on_success(unit_of_work: UnitOfWork, mock_session: AsyncMock) -> None:
    """
    Test that the `__aexit__` method calls `commit` when no exception occurs.

    Steps:
    1. Arrange: Prepare a UnitOfWork instance with a mocked session.
    2. Act: Use `async with` and ensure no exception is raised.
    3. Assert: Verify that `commit` is called, and `rollback` is not.
    """
    # Act
    async with unit_of_work:
        pass  # No exception occurs

    # Assert
    mock_session.commit.assert_awaited_once()
    mock_session.rollback.assert_not_awaited()
