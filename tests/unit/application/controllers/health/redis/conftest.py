from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.application.dependency.use_cases.heakth_check import get_health_check_use_case_redis
from app.main import app


@pytest.fixture
def mock_health_check_use_case_redis():
    """Mock Redis HealthCheckUseCase."""
    mock_use_case = AsyncMock()
    mock_use_case.execute = AsyncMock(return_value={"status": "healthy"})
    return mock_use_case


@pytest.fixture
def test_client(mock_health_check_use_case_redis):
    """Create a test client with mocked dependencies for Redis health check."""

    app.dependency_overrides[get_health_check_use_case_redis] = lambda: mock_health_check_use_case_redis

    return TestClient(app)
