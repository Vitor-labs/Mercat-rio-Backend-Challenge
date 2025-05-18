from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.certidao import Certidao
from app.use_cases.interface import ModelUseCaseInterface


class CertidaoUseCases(ModelUseCaseInterface):
    async def create(self, db: AsyncSession, model_data: dict) -> Certidao:
        new_cert = Certidao(**model_data)
        db.add(new_cert)
        await db.commit()
        await db.refresh(new_cert)
        return new_cert

    async def get(self, db: AsyncSession, certidao_id: int) -> Certidao | None:
        result = await db.execute(select(Certidao).where(Certidao.id == certidao_id))
        return result.scalars().first()

    async def update(self, db: AsyncSession, model_id: int, update_data: dict) -> None:
        await db.execute(
            update(Certidao).where(Certidao.id == model_id).values(**update_data)
        )
        await db.commit()

    async def delete(self, db: AsyncSession, model_id: int) -> None:
        await db.execute(delete(Certidao).where(Certidao.id == model_id))
        await db.commit()
