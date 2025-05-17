def consulta_certidoes_api_mock(cpf_cnpj: str):
    return {
        "cpf_cnpj": cpf_cnpj,
        "certidoes": [
            {"tipo": "federal", "status": "negativa", "conteudo_base64": "abc123"},
            {"tipo": "trabalhista", "status": "positiva", "conteudo_base64": "def456"}
        ]
    }
