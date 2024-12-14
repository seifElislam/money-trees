"""
logger module
"""
import logging
from config import ENV
from custom_exceptions import AppException

# Logging configuration
logging.basicConfig(
    level=logging.DEBUG if ENV == "local" else logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error("An error occurred in %s: %s", func.__name__, e, exc_info=ENV == "local")
            raise AppException(e)

    return wrapper
