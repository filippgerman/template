from unittest.mock import AsyncMock

import pytest

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.mark.asyncio
async def test_commit_failure(unit_of_work: UnitOfWork, mock_session: AsyncMock) -> None:
    """
    Test the `commit` method of `UnitOfWork` when the transaction fails.

    This test verifies that an exception raised during `commit` is propagated correctly.

    Steps:
    1. Arrange: Mock the session's `commit` method to raise an exception.
    2. Act: Call the `commit` method and catch the exception.
    3. Assert: Verify that the exception was raised and `commit` was attempted.
    """
    # Arrange
    mock_session.commit.side_effect = Exception("Commit failed")

    # Act & Assert
    with pytest.raises(Exception, match="Commit failed"):
        await unit_of_work.commit()

    mock_session.commit.assert_awaited_once()
