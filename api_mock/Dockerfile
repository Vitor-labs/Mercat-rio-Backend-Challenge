# Usa imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# Expõe a porta da aplicação
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
