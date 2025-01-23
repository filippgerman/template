from unittest.mock import AsyncMock

import pytest

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.mark.asyncio
async def test_aexit_calls_rollback_on_exception(unit_of_work: UnitOfWork, mock_session: AsyncMock) -> None:
    """
    Test that the `__aexit__` method calls `rollback` when an exception occurs.

    Steps:
    1. Arrange: Prepare a UnitOfWork instance with a mocked session.
    2. Act: Use `async with` and raise an exception inside the context.
    3. Assert: Verify that `rollback` is called, and `commit` is not.
    """
    # Act
    with pytest.raises(ValueError, match="Test exception"):
        async with unit_of_work:
            raise ValueError("Test exception")  # Exception occurs

    # Assert
    mock_session.rollback.assert_awaited_once()
    mock_session.commit.assert_not_awaited()
