from fastapi import APIRouter, Depends, status
from src.core.db import get_db_session
from src.controllers.teachers_crud import teachers_crud
from src.schemas import Teacher

router = APIRouter(prefix="/teachers")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_teachers(session=Depends(get_db_session)): ...


@router.put("/", status_code=status.HTTP_201_CREATED)
async def put_teacher(teacher: Teacher, session=Depends(get_db_session)): ...
