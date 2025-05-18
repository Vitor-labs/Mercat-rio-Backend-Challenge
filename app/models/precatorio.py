from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Precatorio(Base):
    __tablename__ = "precatorios"

    id = Column(Integer, primary_key=True)
    numero_precatorio = Column(String(100), nullable=False)
    valor_nominal = Column(Float, nullable=False)
    foro = Column(String(100), nullable=False)
    data_publicacao = Column(DateTime, nullable=False)

    credor_id = Column(Integer, ForeignKey("credores.id"), nullable=False)
    credor = relationship("Credor", back_populates="precatorios")
