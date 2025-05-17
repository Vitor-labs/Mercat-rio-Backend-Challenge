from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base import Base, OrigemCertidao, StatusCertidao, TipoCertidao


class Certidão(Base):
    __tablename__ = "certidoes"

    id = Column(Integer, primary_key=True)
    tipo = Column(Enum(TipoCertidao), nullable=False)
    origem = Column(Enum(OrigemCertidao), nullable=False)
    arquivo_url = Column(String(500), nullable=True)
    conteudo_base64 = Column(Text, nullable=True)
    status = Column(Enum(StatusCertidao), nullable=False)
    recebida_em = Column(DateTime, default=datetime.now)

    credor_id = Column(Integer, ForeignKey("credores.id"), nullable=False)

    credor = relationship("Credor", back_populates="certidoes")
