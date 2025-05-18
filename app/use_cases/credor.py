from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.creador import Credor
from app.use_cases.interface import ModelUseCaseInterface


class CredorUseCases(ModelUseCaseInterface):
    async def create(self, db: AsyncSession, model_data: dict) -> Credor:
        new_credor = Credor(**model_data)
        db.add(new_credor)
        await db.commit()
        await db.refresh(new_credor)
        return new_credor

    async def read(self, db: AsyncSession, model_id: int) -> Credor | None:
        result = await db.execute(select(Credor).where(Credor.id == model_id))
        return result.scalars().first()

    async def update(self, db: AsyncSession, model_id: int, update_data: dict) -> None:
        await db.execute(
            update(Credor).where(Credor.id == model_id).values(**update_data)
        )
        await db.commit()

    async def delete(self, db: AsyncSession, model_id: int) -> None:
        await db.execute(delete(Credor).where(Credor.id == model_id))
        await db.commit()
