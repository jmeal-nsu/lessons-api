from datetime import time
from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Any
from src.models.lesson import LessonType, DayOfAWeek
from src.schemas.column_types import timeHHMM


class Lesson(BaseModel):
    subject: str = Field(examples=["ТПНС"])
    type: LessonType
    week_day: DayOfAWeek
    start: timeHHMM
    teacher_id: int = Annotated[int, Field(gt=0)]
    place_id: int = Annotated[int, Field(gt=0)]

    @field_validator("start")
    @classmethod
    def validate(cls: BaseModel, value: str) -> time:
        return time(*list(map(int, value.split(":"))), 0, 0)
