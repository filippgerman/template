import pytest

from app.core.errors.database_error import DatabaseNotReachable


@pytest.mark.asyncio
async def test_health_check_db_failure(test_client, mock_health_check_use_case):
    """
    Test the behavior of the /health/db endpoint when the database is unreachable.

    This test verifies the following:
    1. The endpoint raises an HTTP 503 Service Unavailable error if the database is not reachable.
    2. The error message provided by the DatabaseNotReachable exception is returned in the response.
    3. The mocked HealthCheckUseCase's `execute` method is called exactly once.

    Steps:
    - Mock the `execute` method of the HealthCheckUseCase to raise a `DatabaseNotReachable` exception.
    - Send a GET request to the /health/db endpoint using the test client.
    - Validate the response:
      - Ensure the status code is 503.
      - Verify the JSON body contains the expected "detail" key with the correct error message.
    - Confirm that the mocked `execute` method was invoked once.

    Expected Behavior:
    - The API should return a 503 status code and the error message "Database is unreachable."
    - The `execute` method of the mocked use case should be awaited exactly once.
    """
    # Arrange
    mock_health_check_use_case.execute.side_effect = DatabaseNotReachable("Database is unreachable")

    # Act
    response = test_client.get("/health/db")

    # Assert
    assert response.status_code == 503
    assert response.json() == {"detail": "Database is unreachable"}
    mock_health_check_use_case.execute.assert_called_once()
