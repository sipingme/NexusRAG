from enum import Enum
import coloredlogs
import logging

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

def initialize_logger(log_level: LogLevel) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level.value)
    coloredlogs.install(level=log_level.value, logger=logger)
    return logger