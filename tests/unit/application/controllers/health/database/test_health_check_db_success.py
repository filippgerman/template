import pytest


@pytest.mark.asyncio
async def test_health_check_db_success(test_client, mock_health_check_use_case):
    """
    Test successful health check for the database.
    Ensures that the endpoint returns a 200 status code and expected JSON.
    """
    # Arrange
    mock_health_check_use_case.execute.return_value = {"status": "healthy"}

    # Act
    response = test_client.get("/health/db")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    mock_health_check_use_case.execute.assert_called_once()
