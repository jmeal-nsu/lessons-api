from sqlalchemy import Column, Integer, String
from src.core.db import PostgresBase


class Teacher(PostgresBase):

    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
