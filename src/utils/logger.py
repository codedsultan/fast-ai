import logging
import sys
from pathlib import Path

import yaml
from loguru import logger

# Path to logging_config.yaml
CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "config" / "logging_config.yaml"


class InterceptHandler(logging.Handler):
    """
    Redirect standard logging (e.g., from FastAPI, Uvicorn, SQLAlchemy) into Loguru.
    """

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except Exception:
            level = "INFO"

        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(level, record.getMessage())


def load_logging_config():
    """
    Load YAML logging configuration from config/logging_config.yaml.
    """
    if not CONFIG_PATH.exists():
        logger.warning(f"Logging config not found at {CONFIG_PATH}, using default console logger.")
        return None

    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


def setup_logging():
    """
    Configure Loguru according to YAML config and intercept std logging.
    """
    config = load_logging_config()

    # Clear default Loguru handlers
    logger.remove()

    if config and "loguru" in config:
        handlers = config["loguru"].get("handlers", [])
        json_handler = config["loguru"].get("json_handler", None)

        # Register plain-text handlers
        for handler in handlers:
            logger.add(
                handler["sink"],
                level=handler.get("level", "INFO"),
                format=handler.get("format"),
                rotation=handler.get("rotation"),
                retention=handler.get("retention"),
                compression=handler.get("compression"),
                backtrace=handler.get("backtrace", False),
                diagnose=handler.get("diagnose", False),
            )

        # Register JSON handler if defined
        if json_handler:
            logger.add(
                json_handler["sink"],
                level=json_handler.get("level", "INFO"),
                serialize=True,
                rotation=json_handler.get("rotation", None),
                retention=json_handler.get("retention", None),
                compression=json_handler.get("compression", None),
            )
    else:
        # Fallback to console-only
        logger.add(sys.stdout, level="INFO")

    # Redirect standard logging to Loguru
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = [InterceptHandler()]

    # Startup confirmation log
    logger.info("Logging successfully configured using Loguru.")


# Run setup immediately on import
setup_logging()
