from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_endpoint():
    response = client.get("/add", params={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_divide_by_zero_returns_400():
    response = client.get("/divide", params={"a": 10, "b": 0})

    assert response.status_code == 400
