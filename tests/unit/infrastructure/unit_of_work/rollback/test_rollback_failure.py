from unittest.mock import AsyncMock

import pytest

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.mark.asyncio
async def test_rollback_failure(unit_of_work: UnitOfWork, mock_session: AsyncMock) -> None:
    """
    Test the `rollback` method of `UnitOfWork` when the rollback fails.

    This test verifies that an exception raised during `rollback` is propagated correctly.

    Steps:
    1. Arrange: Mock the session's `rollback` method to raise an exception.
    2. Act: Call the `rollback` method and catch the exception.
    3. Assert: Verify that the exception was raised and `rollback` was attempted.
    """
    # Arrange
    mock_session.rollback.side_effect = Exception("Rollback failed")

    # Act & Assert
    with pytest.raises(Exception, match="Rollback failed"):
        await unit_of_work.rollback()

    mock_session.rollback.assert_awaited_once()
