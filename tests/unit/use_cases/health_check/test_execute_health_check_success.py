from unittest.mock import AsyncMock

import pytest

from app.core.use_cases.health_check import HealthCheckUseCase


@pytest.mark.asyncio
async def test_execute_health_check_success(
    health_check_use_case: HealthCheckUseCase, mock_health_checker: AsyncMock
) -> None:
    """
    Test the `execute` method of `HealthCheckUseCase` for a successful health check.

    This test verifies that the `execute` method returns the correct health status when the health checker succeeds.

    Steps:
    1. Arrange: Mock the health checker to return a successful status.
    2. Act: Call the `execute` method.
    3. Assert: Verify that the returned status matches the mock result.
    """
    # Arrange
    mock_health_checker.check_health = AsyncMock(return_value={"status": "healthy"})

    # Act
    result = await health_check_use_case.execute()

    # Assert
    assert result == {"status": "healthy"}
