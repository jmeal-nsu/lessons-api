from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import mapped_column, relationship

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
    start = Column(DateTime)
    subject = Column(String)
    type = Column(ENUM(LessonType, create_type=True), nullable=False)
    teacher_id = mapped_column(ForeignKey("teacher.id"), nullable=False)
    teacher = relationship("Teacher")
    place_id = mapped_column(ForeignKey("place.id"), nullable=False)
    place = relationship("Place")
