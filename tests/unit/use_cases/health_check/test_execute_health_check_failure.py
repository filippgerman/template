from unittest.mock import AsyncMock

import pytest

from app.core.use_cases.health_check import HealthCheckUseCase


@pytest.mark.asyncio
async def test_execute_health_check_failure(
    health_check_use_case: HealthCheckUseCase, mock_health_checker: AsyncMock
) -> None:
    """
    Test the `execute` method of `HealthCheckUseCase` for a failed health check.

    This test verifies that the `execute` method raises an exception when the health checker fails.

    Steps:
    1. Arrange: Mock the health checker to raise an exception.
    2. Act: Call the `execute` method.
    3. Assert: Verify that the exception is propagated correctly.
    """
    # Arrange
    mock_health_checker.check_health = AsyncMock(side_effect=Exception("Health check failed"))

    # Act & Assert
    with pytest.raises(Exception, match="Health check failed"):
        await health_check_use_case.execute()
