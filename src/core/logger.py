import colorlog
import sys

from fastapi.logger import logger

logger = colorlog.getLogger()
logger.setLevel(colorlog.DEBUG)
handler = colorlog.StreamHandler(sys.stdout)
handler.setLevel(colorlog.DEBUG)
formater = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)s%(reset)s:\t%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)
handler.setFormatter(formater)
logger.addHandler(handler)
