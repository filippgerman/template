import logging

from app.utils.logging_config import setup_logger


def get_logger() -> logging.Logger:
    """
    Provide a logger instance.

    Returns:
        Logger: Configured logger instance.
    """
    return setup_logger("app", write_to_file=True, log_file_path="./logs/app.log")
