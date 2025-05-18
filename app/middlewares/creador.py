from pydantic import BaseModel, EmailStr, field_validator

from .precatorio import PrecatórioCreate


class CredorBase(BaseModel):
    nome: str
    cpf_cnpj: str
    email: EmailStr
    telefone: str

    @field_validator("cpf_cnpj")
    def cpf_cnpj_must_have_valid_length(cls, v):
        if len(v) < 11 or len(v) > 18:
            raise ValueError("CPF/CNPJ deve ter entre 11 e 18 caracteres")
        return v


class CredorCreate(CredorBase):
    precatorio: PrecatórioCreate


class CredorRead(CredorBase):
    id: int
