from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.documento import DocumentoPessoal
from app.use_cases.interface import ModelUseCaseInterface


class DocumentoUseCases(ModelUseCaseInterface):
    async def create(self, db: AsyncSession, model_data: dict) -> DocumentoPessoal:
        new_doc = DocumentoPessoal(**model_data)
        db.add(new_doc)
        await db.commit()
        await db.refresh(new_doc)
        return new_doc

    async def get(self, db: AsyncSession, model_id: int) -> DocumentoPessoal | None:
        result = await db.execute(
            select(DocumentoPessoal).where(DocumentoPessoal.id == model_id)
        )
        return result.scalars().first()

    async def update(self, db: AsyncSession, model_id: int, update_data: dict) -> None:
        await db.execute(
            update(DocumentoPessoal)
            .where(DocumentoPessoal.id == model_id)
            .values(**update_data)
        )
        await db.commit()

    async def delete(self, db: AsyncSession, model_id: int) -> None:
        await db.execute(
            delete(DocumentoPessoal).where(DocumentoPessoal.id == model_id)
        )
        await db.commit()
