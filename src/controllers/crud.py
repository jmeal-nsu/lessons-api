from typing import Any
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dataclasses import dataclass


@dataclass
class BaseCRUD:
    model: DeclarativeBase

    async def read_all(self, session: AsyncSession) -> tuple[tuple[Any]]:
        querry = select(self.model)
        return (await session.execute(querry)).scalars().all()
