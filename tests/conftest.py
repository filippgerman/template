from unittest.mock import AsyncMock, Mock

import pytest

from app.core.interfaces.services.health_check_interface import IHealthCheck


@pytest.fixture
def mock_http_client():
    """Фикстура для мока HTTP клиента."""
    return AsyncMock()


@pytest.fixture
def mock_logger():
    """Фикстура для мока логгера."""
    return Mock()


@pytest.fixture
def mock_repository():
    """Мок для репозитория токенов."""
    return AsyncMock()


@pytest.fixture
def mock_cache():
    """Мок для кэша."""
    return AsyncMock()


@pytest.fixture
def mock_bank_api():
    """Мок для API банка."""
    return AsyncMock()


@pytest.fixture
def mock_db_session():
    """Mock for the database session."""
    return AsyncMock()


@pytest.fixture
def mock_unit_of_work():
    """Mock for the unit of work."""
    return AsyncMock()


@pytest.fixture
def mock_health_checker() -> AsyncMock:
    """Mock for the health checker service."""
    return AsyncMock(spec=IHealthCheck)
