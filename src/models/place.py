from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from src.core.db import PostgresBase
from enum import Enum

class Pavilion(Enum):
    NEW = "new"
    MAIN = "main"
    LAB = "laboratory"
    SPORT_OLD = "sport_old"
    SPORT_NEW = "sport_new"
    STADIUM = "stadium"
class Place(PostgresBase):

    __tablename__ = "place"

    id = Column(Integer, primary_key=True)
    cabinet = Column(String)
    pavilion = Column(ENUM(Pavilion, create_type=True), nullable=True)
