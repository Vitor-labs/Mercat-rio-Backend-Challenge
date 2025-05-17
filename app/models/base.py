import enum

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TipoDocumento(enum.Enum):
    identidade = "identidade"
    comprovante_residencia = "comprovante_residencia"


class TipoCertidao(enum.Enum):
    federal = "federal"
    estadual = "estadual"
    municipal = "municipal"
    trabalhista = "trabalhista"


class OrigemCertidao(enum.Enum):
    manual = "manual"
    api = "api"


class StatusCertidao(enum.Enum):
    negativa = "negativa"
    positiva = "positiva"
    invalida = "invalida"
    pendente = "pendente"
