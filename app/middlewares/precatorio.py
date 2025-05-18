from datetime import datetime

from pydantic import BaseModel


class PrecatórioBase(BaseModel):
    numero_precatorio: str
    valor_nominal: float
    foro: str
    data_publicacao: datetime


class PrecatórioCreate(PrecatórioBase):
    credor_id: int | None = None  # preenchido internamente se aninhado


class PrecatórioRead(PrecatórioBase):
    id: int

    class Config:
        orm_mode = True
