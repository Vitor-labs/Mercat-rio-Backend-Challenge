# Mercatório Backend Challenge

## Descrição

Neste desafio, você irá desenvolver uma API REST que simula a etapa de **originação de precatórios** na Mercatório. O objetivo é construir um sistema que permita o cadastro de credores, seus respectivos precatórios, upload de documentos pessoais e a obtenção de certidões de forma manual ou automática (via API mockada).

Essa API simula parte do fluxo de análise inicial de viabilidade jurídica e documental dos direitos creditórios.

## Funcionalidades esperadas

* Cadastro de **credor** com dados pessoais
* Cadastro de **precatório** vinculado a um credor
* Upload de **documentos pessoais** (ex: identidade, comprovante de residência)
* Upload manual de **certidões**
* Simulação de obtenção automática de certidões via API mockada
* Consulta de um credor com seus documentos e certidões

## Requisitos obrigatórios

* Utilizar uma das linguagens: **Python** ou **Ruby**.
* Endpoints RESTful bem definidos
* Upload de arquivos (armazenamento local ou temporário)
* Implementar uma API mock local para simular a busca de certidões
* Documentação de como rodar o projeto localmente

## Requisitos desejáveis

* Validação de extensões e tamanho de arquivos
* Job que revalida certidões automaticamente a cada 24h
* Interface web simples para upload/visualização
* Dockerfile e/ou docker-compose
* Testes automatizados

## Entidades principais

### Credor

* `id`
* `nome`
* `cpf_cnpj`
* `email`
* `telefone`

### Precatório

* `id`
* `credor_id`
* `numero_precatorio`
* `valor_nominal`
* `foro`
* `data_publicacao`

### Documento Pessoal

* `id`
* `credor_id`
* `tipo` (`identidade`, `comprovante_residencia`, etc.)
* `arquivo_url`
* `enviado_em`

### Certidão

* `id`
* `credor_id`
* `tipo` (`federal`, `estadual`, `municipal`, `trabalhista`)
* `origem` (`manual`, `api`)
* `arquivo_url` ou `conteudo_base64`
* `status` (`negativa`, `positiva`, `invalida`, `pendente`)
* `recebida_em`

## Endpoints esperados

* `POST /credores` – Cadastra credor e seu precatório
* `POST /credores/:id/documentos` – Upload de documentos pessoais
* `POST /credores/:id/certidoes` – Upload manual de certidões
* `POST /credores/:id/buscar-certidoes` – Simula consulta de certidões via API
* `GET /credores/:id` – Consulta geral do credor, precatório, documentos e certidões

## API Mock - Consulta de certidões

Deve ser implementada uma API local com o seguinte endpoint:

```
GET /api/certidoes?cpf_cnpj=00000000000
```

Resposta esperada:

```json
{
  "cpf_cnpj": "00000000000",
  "certidoes": [
    {
      "tipo": "federal",
      "status": "negativa",
      "conteudo_base64": "..."
    },
    {
      "tipo": "trabalhista",
      "status": "positiva",
      "conteudo_base64": "..."
    }
  ]
}
```

## Exemplo de payload - `POST /credores`

```json
{
  "nome": "Maria Silva",
  "cpf_cnpj": "12345678900",
  "email": "maria@example.com",
  "telefone": "11999999999",
  "precatorio": {
    "numero_precatorio": "0001234-56.2020.8.26.0050",
    "valor_nominal": 50000.00,
    "foro": "TJSP",
    "data_publicacao": "2023-10-01"
  }
}
```

## Como enviar

1. Crie um repositório público no GitHub ou GitLab
2. Suba o seu código com README contendo:

   * Instruções para executar a API e a API mock
   * Exemplos de requisições (curl, httpie, Postman ou Swagger)
3. Envie o link do repositório

## Observações:

* **Avaliação:** O código será avaliado quanto à qualidade, boas práticas de desenvolvimento, arquitetura, e a capacidade de atender aos requisitos propostos.

Boa sorte! Qualquer dúvida, entre em contato com o time da Mercatório.
