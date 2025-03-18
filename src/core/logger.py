"""Logging configuration for the application."""

import logging
import sys
from typing import Any, Dict

from pythonjsonlogger import jsonlogger


def setup_logging(
    level: str = "INFO",
    json_format: bool = False,
    log_config: Dict[str, Any] = None,
) -> None:
    """Set up logging configuration.
    
    Args:
        level: Logging level (default: INFO)
        json_format: Whether to use JSON formatting (default: False)
        log_config: Additional logging configuration (default: None)
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    if json_format:
        formatter = jsonlogger.JsonFormatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(message)s"
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # Apply additional config if provided
    if log_config:
        logging.config.dictConfig(log_config)

    # Suppress noisy loggers
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy").setLevel(logging.WARNING) 