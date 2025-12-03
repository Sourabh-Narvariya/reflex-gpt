"""Logging configuration for Reflex-GPT.

Provides structured logging with proper formatting and level management.
"""

import logging
import logging.handlers
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)


def setup_logging(level: str = "INFO") -> logging.Logger:
    """Configure application logging.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        
    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger("reflex_gpt")
    logger.setLevel(getattr(logging, level.upper()))
    
    # Create formatter
    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler (rotating)
    log_file = os.path.join(LOGS_DIR, f"app_{datetime.now():%Y%m%d}.log")
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10_485_760,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger


# Initialize logger
logger = setup_logging(os.getenv("LOG_LEVEL", "INFO"))
