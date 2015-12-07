import logging
from sling.core import config


logger = logging.getLogger('sling')


def install_module(app):
    log_level = getattr(logging, config.LOG_LEVEL)
    log_format = config.LOG_FORMAT
    log_timestamp_format = config.LOG_TIMESTAMP_FORMAT
    logging.basicConfig(
        format=log_format,
        datefmt=log_timestamp_format,
        level=log_level,
    )
