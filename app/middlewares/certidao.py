from datetime import datetime

from pydantic import BaseModel

from app.models.base import OrigemCertidao, StatusCertidao, TipoCertidao


class CertidaoBase(BaseModel):
    tipo: TipoCertidao
    origem: OrigemCertidao
    status: StatusCertidao
    arquivo_url: str | None = None
    conteudo_base64: str | None = None


class CertidaoCreate(CertidaoBase):
    credor_id: int


class CertidaoRead(CertidaoBase):
    id: int
    recebida_em: datetime

    class Config:
        orm_mode = True
