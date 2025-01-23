import logging
from typing import Optional


class CustomLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        extra = kwargs.pop("extra", {})
        log_extra = {**self.extra, **extra} if self.extra else extra
        if log_extra:
            msg = f"{msg} | extra: {log_extra}"
        return msg, kwargs


def setup_logger(
    name: str = "app_logger",
    level: str = "INFO",
    write_to_file: bool = False,
    log_file_path: Optional[str] = "./logs/app.log",
) -> logging.LoggerAdapter:
    """
    Set up a logger with optional file logging.

    Args:
        name (str): Logger name.
        level (str): Logging level (e.g., "INFO", "DEBUG").
        write_to_file (bool): Whether to write logs to a file.
        log_file_path (str): Path to the log file (used if write_to_file=True).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level.upper())

    log_formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Remove existing handlers to prevent duplication
    if logger.hasHandlers():
        logger.handlers.clear()

    # Add console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # Add file handler if enabled
    if write_to_file and log_file_path:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)

    return CustomLoggerAdapter(logger, extra={})
