from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base, TipoDocumento


class DocumentoPessoal(Base):
    __tablename__ = "documentos_pessoais"

    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey("credores.id"), nullable=False)
    tipo = Column(Enum(TipoDocumento), nullable=False)
    arquivo_url = Column(String(500), nullable=False)
    enviado_em = Column(DateTime, default=datetime.now)

    credor = relationship("Credor", back_populates="documentos")
