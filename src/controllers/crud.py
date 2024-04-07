from typing import Any, overload
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class BaseCRUD:
    model: DeclarativeBase

    async def read_all(
        self, session: AsyncSession, *, without_id=False
    ) -> tuple[tuple[Any]]:
        querry = select(self.model)
        rows = (await session.execute(querry)).scalars().all()

        if not hasattr(rows[0], "id"):
            return rows

        if without_id:
            for row in rows:
                del row.id

        return rows

    @overload
    async def insert(self, session: AsyncSession, data: BaseModel): ...
    @overload
    async def insert(self, session: AsyncSession, data: list[BaseModel]): ...

    async def insert(self, session: AsyncSession, data: list[BaseModel] | BaseModel):
        if not isinstance(data, list):
            data = [data]
        querry = insert(self.model).values([dict(row) for row in data])
        await session.execute(querry)
        await session.commit()
