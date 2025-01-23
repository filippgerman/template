import logging

from app.utils.logging_config import setup_logger


def test_setup_logger_file(tmp_path):
    log_file = tmp_path / "test.log"
    logger = setup_logger(name="test_logger", level="INFO", write_to_file=True, log_file_path=str(log_file))

    # Check if file handler is added
    assert any(isinstance(handler, logging.FileHandler) for handler in logger.logger.handlers)

    # Log a message and check if it is written to the file
    logger.info("Test message")
    with open(log_file, "r") as f:
        log_content = f.read()
    assert "Test message" in log_content
