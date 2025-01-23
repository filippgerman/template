from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from app.application.dependency.use_cases.heakth_check import get_health_check_use_case_db
from app.main import app


@pytest.fixture
def mock_health_check_use_case():
    """
    Fixture to create a mock for the HealthCheckUseCase.
    The `execute` method returns a successful health status.
    """
    mock_use_case = AsyncMock()
    mock_use_case.execute = AsyncMock(return_value={"status": "healthy"})
    return mock_use_case


@pytest.fixture
def test_client(mock_health_check_use_case):
    """
    Fixture to create a FastAPI test client with overridden dependencies.
    The `get_health_check_use_case_db` dependency is mocked.
    """
    # Override the dependency for the health check use case
    app.dependency_overrides[get_health_check_use_case_db] = lambda: mock_health_check_use_case
    return TestClient(app)
