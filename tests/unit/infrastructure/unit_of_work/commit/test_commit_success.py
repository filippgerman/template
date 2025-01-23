from unittest.mock import AsyncMock

import pytest

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.mark.asyncio
async def test_commit_success(unit_of_work: UnitOfWork, mock_session: AsyncMock) -> None:
    """
    Test the `commit` method of `UnitOfWork` for a successful transaction.

    This test verifies that the `commit` method calls the session's `commit` method.

    Steps:
    1. Arrange: Set up the UnitOfWork with a mocked session.
    2. Act: Call the `commit` method.
    3. Assert: Verify that the session's `commit` method was called once.
    """
    # Act
    await unit_of_work.commit()

    # Assert
    mock_session.commit.assert_awaited_once()
