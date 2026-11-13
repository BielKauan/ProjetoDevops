# ESTAGIO 1: ambiente de testes
FROM python:3.14-slim AS test

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY tests/ ./tests/
COPY conftest.py .

CMD ["python", "-m", "pytest", "-v"]

#ESTAGIO 2: Imagem final de execução
FROM python:3.14-slim AS runtime

WORKDIR /app

COPY app/ ./app/

CMD ["python", "-u", "app/monitor.py"]