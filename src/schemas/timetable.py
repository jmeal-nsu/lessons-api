from typing import Annotated
from pydantic import BaseModel, Field, HttpUrl
from src.models.lesson import LessonType, DayOfAWeek
from src.models.place import Pavilion

Teacher = Annotated[
    str,
    Field(
        pattern=r"(\w+ ){1,2}\w*",
        examples=[
            "Bibov Ibrahim Aranovich",
            "Dadayanow Abrham",
        ],
    ),
]
Cabinet = Annotated[str, Field(pattern=r"\d{1,4}\w*", examples=["2134т"])]
timeHHMM = Annotated[str, Field(pattern=r"([0-1]\d|2[0-3]):[0-5]\d")]


class TimeTableItem(BaseModel):
    subject: str = Field(examples=["ТПНС"])
    type: LessonType
    week_day: DayOfAWeek
    start: timeHHMM
    cabinet: Cabinet | HttpUrl
    pavilion: Pavilion
    teacher: Teacher
