from fastapi import FastAPI, HTTPException

from app.calculator import add, divide

app = FastAPI(title="Python API")


@app.get("/")
def home():
    return {"message": "Welcome to Python API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/add")
def add_numbers(a: float, b: float):
    return {"result": add(a, b)}


@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        return {"result": divide(a, b)}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
