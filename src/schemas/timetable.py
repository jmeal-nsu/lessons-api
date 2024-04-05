from pydantic import BaseModel, Field, HttpUrl

from src.models.lesson import LessonType, DayOfAWeek
from src.models.place import Pavilion
from src.schemas.column_types import timeHHMM, Teacher, Cabinet


class TimeTableItem(BaseModel):
    subject: str = Field(examples=["ТПНС"])
    type: LessonType
    week_day: DayOfAWeek
    start: timeHHMM
    cabinet: Cabinet | HttpUrl | None
    pavilion: Pavilion | None
    teacher: Teacher
