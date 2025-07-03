FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install streamlit requests

ENV BACKEND_URL=https://your-backend-service.a.run.app
EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s CMD python -c "import requests; requests.get('http://localhost:8501/_stcore/health')"

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]