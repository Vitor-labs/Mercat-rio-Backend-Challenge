import base64
import random
from datetime import datetime
from enum import Enum

from faker import Faker
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
faker = Faker()


class TipoCertidao(str, Enum):
    federal = "federal"
    estadual = "estadual"
    municipal = "municipal"
    trabalhista = "trabalhista"


class OrigemCertidao(str, Enum):
    manual = "manual"
    api = "api"


class StatusCertidao(str, Enum):
    negativa = "negativa"
    positiva = "positiva"
    invalida = "invalida"
    pendente = "pendente"


class Certidao(BaseModel):
    id: int
    tipo: TipoCertidao
    origem: OrigemCertidao
    arquivo_url: str | None
    conteudo_base64: str | None
    status: StatusCertidao
    recebida_em: datetime


def gerar_certidao_fake(id: int) -> Certidao:
    arquivo_falso = faker.text(max_nb_chars=100).encode("utf-8")
    return Certidao(
        id=id,
        tipo=random.choice(list(TipoCertidao)),
        origem=random.choice(list(OrigemCertidao)),
        arquivo_url=faker.url(),
        conteudo_base64=base64.b64encode(arquivo_falso).decode("utf-8"),
        status=random.choice(list(StatusCertidao)),
        recebida_em=faker.date_time_this_year(),
    )


@app.get("/api/certidoes", response_model=list[Certidao])
def listar_certidoes_fake(qtd: int = 5):
    return [gerar_certidao_fake(i) for i in range(1, qtd + 1)]
