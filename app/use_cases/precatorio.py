from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.precatorio import Precatorio
from app.use_cases.interface import ModelUseCaseInterface


class PrecatorioUseCases(ModelUseCaseInterface):
    async def create(self, db: AsyncSession, model_data: dict):
        new_precatorio = Precatorio(**model_data)
        db.add(new_precatorio)
        await db.commit()
        await db.refresh(new_precatorio)
        return new_precatorio

    async def get(self, db: AsyncSession, model_id: int):
        result = await db.execute(select(Precatorio).where(Precatorio.id == model_id))
        return result.scalars().first()

    async def update(self, db: AsyncSession, model_id: int, update_data: dict):
        await db.execute(
            update(Precatorio).where(Precatorio.id == model_id).values(**update_data)
        )
        await db.commit()

    async def delete(self, db: AsyncSession, model_id: int):
        await db.execute(delete(Precatorio).where(Precatorio.id == model_id))
        await db.commit()
