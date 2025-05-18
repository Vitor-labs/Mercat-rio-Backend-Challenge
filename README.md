✅ Endpoints Implementados

| Método | Rota                              | Descrição                                   |
| ------ | --------------------------------- | ------------------------------------------- |
| `POST` | `/credores`                       | Cadastra credor e precatório                |
| `POST` | `/credores/{id}/documentos`       | Upload de documentos                        |
| `POST` | `/credores/{id}/certidoes`        | Upload manual de certidões                  |
| `POST` | `/credores/{id}/buscar-certidoes` | Consulta simulada via API mock              |
| `GET`  | `/credores/{id}`                  | Consulta completa do credor                 |
| `GET`  | `/api/certidoes`                  | API mock (local) para consulta de certidões |
