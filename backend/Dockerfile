FROM python:3.9-slim
WORKDIR /app
# Copy everything from the current directory (backend/)
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]