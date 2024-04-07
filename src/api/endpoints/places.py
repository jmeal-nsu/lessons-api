from fastapi import APIRouter, Depends, status
from src.core.db import get_db_session
from src.controllers.places_crud import places_crud
from src.schemas import OfflinePlace, OnlinePlace

router = APIRouter(prefix="/places")

Place = OfflinePlace | OnlinePlace


@router.get("/", status_code=status.HTTP_200_OK)
async def get_places(
    session=Depends(get_db_session),
) -> list[OnlinePlace | OfflinePlace]:
    return await places_crud.read_all(session, without_id=True)


@router.put("/", status_code=status.HTTP_201_CREATED)
async def put_place(place: list[Place] | Place, session=Depends(get_db_session)):
    await places_crud.insert(session, place)
