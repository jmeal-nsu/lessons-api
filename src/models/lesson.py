from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM, TIME
from sqlalchemy.orm import relationship

from src.core.db import PostgresBase
from enum import Enum


class DayOfAWeek(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class LessonType(Enum):
    LECTURE = "Lecture"
    PRACTICE = "Practice"
    LABORATORY = "Laboratory"


class Lesson(PostgresBase):

    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True)
    day = Column(ENUM(DayOfAWeek, create_type=True), nullable=False)
    start = Column(TIME)
    subject = Column(String)
    type = Column(ENUM(LessonType, create_type=True), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False)
    teacher = relationship("Teacher")
    place_id = Column(Integer, ForeignKey("place.id"), nullable=False)
    place = relationship("Place")
