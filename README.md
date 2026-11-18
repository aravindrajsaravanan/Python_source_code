# Python API

A small FastAPI application.

## Endpoints

| URL | What it does |
|---|---|
| `/` | Welcome message |
| `/health` | Health check, returns `{"status": "ok"}` |
| `/add?a=2&b=3` | Adds two numbers |
| `/divide?a=10&b=2` | Divides two numbers |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs

## Checks before pushing

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

## Docker

```bash
docker build -t python-api .
docker run -p 8000:8000 python-api
```
