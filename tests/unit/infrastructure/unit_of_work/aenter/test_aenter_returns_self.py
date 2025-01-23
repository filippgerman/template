import pytest

from app.infrastructure.database.unit_of_work import UnitOfWork


@pytest.mark.asyncio
async def test_aenter_returns_self(unit_of_work: UnitOfWork) -> None:
    """
    Test that the `__aenter__` method returns the UnitOfWork instance.

    Steps:
    1. Arrange: Prepare a UnitOfWork instance.
    2. Act: Use `async with` and capture the returned value.
    3. Assert: Verify that `__aenter__` returns the same instance.
    """
    # Act
    async with unit_of_work as uow:
        # Assert
        assert uow is unit_of_work
