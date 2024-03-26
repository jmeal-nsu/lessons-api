from src.core.config import AppSettings
import colorlog

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)s%(reset)s:\t\t%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

logger = colorlog.getLogger(__name__)

logger.setLevel(AppSettings.log_level)
console_handler = colorlog.StreamHandler()
console_handler.setLevel(AppSettings.log_level)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
