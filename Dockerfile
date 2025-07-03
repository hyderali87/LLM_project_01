# Dockerfile (backend)
FROM python:3.10
WORKDIR /app
COPY backend/ .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

# Dockerfile.frontend
FROM python:3.10
WORKDIR /app
COPY frontend/ .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]