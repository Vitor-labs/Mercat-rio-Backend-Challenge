from fastapi import APIRouter, UploadFile, File, Depends
from app.use_cases.credores import criar_credor, buscar_credor_completo
from app.use_cases.certidoes import buscar_certidoes_mockadas

router = APIRouter()

@router.post("/")
def cadastrar_credor(data: dict):
    return criar_credor(data)

@router.post("/{credor_id}/buscar-certidoes")
def buscar_certidoes(credor_id: int):
    return buscar_certidoes_mockadas(credor_id)

@router.get("/{credor_id}")
def consultar_credor(credor_id: int):
    return buscar_credor_completo(credor_id)
