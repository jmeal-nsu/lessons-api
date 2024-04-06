from typing import Any
from pydantic import BaseModel, HttpUrl, field_validator

from src.models.place import Pavilion
from src.schemas.column_types import Cabinet


class OfflinePlace(BaseModel):
    cabinet: Cabinet | None
    pavilion: Pavilion


class OnlinePlace(BaseModel):
    cabinet: HttpUrl
    pavilion: None

    @field_validator("cabinet")
    @classmethod
    def validate_cabinet(cls, value: str) -> str:
        return str(HttpUrl(value))
