from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import validator
from enum import Enum
from urllib.parse import quote
import colorlog


class ColorLogLevel(Enum):
    INFO = colorlog.INFO
    DEBUG = colorlog.DEBUG
    WARNING = colorlog.WARNING
    ERROR = colorlog.ERROR
    CRITICAL = colorlog.CRITICAL


@lambda _: _()
class AppSettings(BaseSettings):
    log_level: int

    @validator("log_level", pre=True)
    @classmethod
    def validate_log_level(cls, level: str) -> int:
        return ColorLogLevel.__members__.get(level.upper()).value

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="APP_", extra="ignore"
    )


@lambda _: _()
class PostgresSettings(BaseSettings):
    host: str
    port: int
    username: str
    password: str
    database: str

    @property
    def uri(self):
        pswd = quote(self.password).replace("%", "%%")
        return f"postgresql+asyncpg://{self.username}:{pswd}@{self.host}:{self.port}/{self.database}"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="PG_", extra="ignore")
