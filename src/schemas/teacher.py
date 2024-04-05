from pydantic import BaseModel

from src.schemas.column_types import Name, Surname, Patronymic


class Teacher(BaseModel):
    name: Name
    surname: Surname | None
    patronymic: Patronymic | None
