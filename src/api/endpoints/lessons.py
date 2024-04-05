from fastapi import APIRouter, Depends
from src.core.db import get_db_session
from src.controllers.lessons_crud import lessons_crud

router = APIRouter(prefix="/lessons")


@router.get("/timetable")
async def get_timetable(session=Depends(get_db_session)):
    return await lessons_crud.read_all(session, without_id=True)
