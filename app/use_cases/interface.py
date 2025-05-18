from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class ModelUseCaseInterface[T](ABC):
    @abstractmethod
    async def create(self, db: AsyncSession, model_data: dict) -> T:
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    async def read(self, db: AsyncSession, model_id: int) -> T | None:
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    async def update(self, db: AsyncSession, model_id: int, update_data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    async def delete(self, db: AsyncSession, model_id: int) -> None:
        raise NotImplementedError("Subclasses must implement this method.")
