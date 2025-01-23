import os

from app.utils.logging_config import setup_logger


def test_custom_logger_adapter():
    logger = setup_logger(name="test_logger")
    logger.info("Test message", extra={"user": "test_user"})

    # Capture the log output
    with open(os.devnull, "w") as f:
        logger.logger.handlers[0].stream = f
        logger.info("Test message", extra={"user": "test_user"})

    assert logger.extra == {}
