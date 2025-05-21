✅ Endpoints Implementados

| Método | Rota                              | Descrição                                   |
| ------ | --------------------------------- | ------------------------------------------- |
| `POST` | `/credores`                       | Cadastra credor e precatório                |
| `POST` | `/credores/{id}/documentos`       | Upload de documentos                        |
| `POST` | `/credores/{id}/certidoes`        | Upload manual de certidões                  |
| `POST` | `/credores/{id}/buscar-certidoes` | Consulta simulada via API mock              |
| `GET`  | `/credores/{id}`                  | Consulta completa do credor                 |


### API MOCK DE CERTIDÕES:

| Método | Rota                              | Descrição                                   |
| ------ | --------------------------------- | ------------------------------------------- |
| `GET`  | `/api/certidoes`                  | API mock (local) para consulta de certidões |

- API de Certidões Mockadas é uma imagem de FastAPI com apenas um metodo (Get) sem auth
- O script usa a lib Faker pra gerar dados falso semi-aleatorios com base no model de Cetidão
