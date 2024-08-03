import os

from loguru import logger


def configure_logging():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    log_dir = os.path.join(base_dir, "logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger.remove()

    logger.add(
        os.path.join(log_dir, "log_info.log"),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {file}:{line}",
        level="INFO",
        rotation="1 week",
        retention="1 month",
        compression="zip",
    )

    logger.add(
        os.path.join(log_dir, "log_critical.log"),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {file}:{line}",
        level="CRITICAL",
        rotation="1 week",
        retention="1 month",
        compression="zip",
    )
