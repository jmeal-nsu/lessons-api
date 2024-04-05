from fastapi import APIRouter, Depends, status
from src.core.db import get_db_session
from src.controllers.lessons_crud import lessons_crud
from src.schemas import TimeTableItem

router = APIRouter(prefix="/lessons")


@router.get("/timetable")
async def get_timetable(session=Depends(get_db_session)) -> list[TimeTableItem]:
    return await lessons_crud.read_all(session, without_id=True)


@router.put("/", status_code=status.HTTP_201_CREATED)
async def put_lesson(lesson: TimeTableItem, session=Depends(get_db_session)): ...
