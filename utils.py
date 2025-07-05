import logging
import os
from datetime import datetime

def setup_logging():
    """Setup logging configuration."""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'logs/app_{datetime.now().strftime("%Y%m%d")}.log'),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def log_request(func):
    """Decorator to log requests."""
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(f"Request to {func.__name__} started")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Request to {func.__name__} completed successfully")
            return result
        except Exception as e:
            logger.error(f"Request to {func.__name__} failed: {str(e)}")
            raise
    return wrapper
