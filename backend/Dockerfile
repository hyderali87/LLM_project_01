FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PORT=8080
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:${PORT} --workers=2 --timeout=300 --preload"

# Ensure logs go to stdout/stderr
ENV PYTHONUNBUFFERED=1
ENV GUNICORN_ACCESS_LOG=-
ENV GUNICORN_ERROR_LOG=-

EXPOSE $PORT
HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:${PORT}/health || exit 1

CMD ["gunicorn", "app:app"]