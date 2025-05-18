from datetime import datetime

from models.base import TipoDocumento
from pydantic import BaseModel


class DocumentoBase(BaseModel):
    tipo: TipoDocumento
    arquivo_url: str


class DocumentoCreate(DocumentoBase):
    credor_id: int


class DocumentoRead(DocumentoBase):
    id: int
    enviado_em: datetime

    class Config:
        orm_mode = True
