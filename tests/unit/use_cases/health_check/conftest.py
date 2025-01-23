from unittest.mock import AsyncMock

import pytest

from app.core.use_cases.health_check import HealthCheckUseCase


@pytest.fixture
def health_check_use_case(mock_health_checker: AsyncMock) -> HealthCheckUseCase:
    """Fixture for the health check use case."""
    return HealthCheckUseCase(health_checker=mock_health_checker)
