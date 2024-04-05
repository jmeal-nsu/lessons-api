from pydantic import BaseModel, HttpUrl

from src.models.place import Pavilion
from src.schemas.column_types import Cabinet


class OfflinePlace(BaseModel):
    cabinet: Cabinet | None
    pavilion: Pavilion


class OnlinePlace(BaseModel):
    cabinet: HttpUrl
    pavilion: None
