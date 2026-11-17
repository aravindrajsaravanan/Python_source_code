# syntax=docker/dockerfile:1
FROM python:3.15.2-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Unprivileged user; the app never needs root
RUN useradd --create-home --uid 10001 appuser

# Runtime deps first (layer cache). Currently empty, kept for when deps are added.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py cli.py ./

USER appuser
ENTRYPOINT ["python", "/app/cli.py"]
CMD ["--help"]
