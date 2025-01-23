import logging

from app.utils.logging_config import CustomLoggerAdapter, setup_logger


def test_setup_logger_console():
    logger = setup_logger(name="test_logger", level="DEBUG")
    assert isinstance(logger, CustomLoggerAdapter)
    assert logger.logger.name == "test_logger"
    assert logger.logger.level == logging.DEBUG
