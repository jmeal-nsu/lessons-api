from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import ENUM, TIME

from src.core.db import PostgresBase
from src.models.lesson import LessonType, DayOfAWeek
from src.models.place import Pavilion


class LessonsWithPlacesAndTeachers(PostgresBase):

    __tablename__ = "lessons_with_places_and_teachers"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    type = Column(ENUM(LessonType, create_type=True), nullable=False)
    week_day = Column(ENUM(DayOfAWeek, create_type=True), nullable=False)
    start = Column(TIME, nullable=False)
    cabinet = Column(String, nullable=True)
    pavilion = Column(ENUM(Pavilion, create_type=True), nullable=True)
    teacher = Column(String)
