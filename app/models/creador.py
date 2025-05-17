from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Credor(Base):
    __tablename__ = "credores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    cpf_cnpj = Column(String(20), nullable=False, unique=True)
    email = Column(String(255), nullable=False)
    telefone = Column(String(20), nullable=False)

    precatorios = relationship(
        "Precatório", back_populates="credor", cascade="all, delete-orphan"
    )
    documentos = relationship(
        "DocumentoPessoal", back_populates="credor", cascade="all, delete-orphan"
    )
    certidoes = relationship(
        "Certidão", back_populates="credor", cascade="all, delete-orphan"
    )
