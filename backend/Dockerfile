FROM python:3.9-slim
WORKDIR /app
# Copy everything from the current directory (backend/)
COPY . .
RUN pip install -r requirements.txt
ENV PORT=8080
EXPOSE $PORT
# Health check endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:$PORT/health || exit 1
# Use explicit IP binding
CMD ["gunicorn", "--bind", "0.0.0.0:${PORT}", "--timeout", "120", "app:app"]