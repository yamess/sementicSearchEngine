import logging.config

logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "colored_formatter": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(asctime)s [%(log_color)s%(levelname)-8s%(reset)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "log_colors": {
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        },
        "file_formatter": {
            "format": "%(asctime)s [%(levelname)-8s] %(module)s:%(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "colored_formatter",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "file_formatter",
            "filename": "app.log",
        },
    },
    "root": {"level": "INFO", "handlers": ["console", "file"]},
}


def set_logger_config():
    logging.config.dictConfig(config=logger_config)
    logger = logging.getLogger(__name__)
    logger.info("Logger initialized")
