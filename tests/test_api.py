from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200

def test_run():
    response = client.post("/v1/run", json={"value": "demo"})
    assert response.status_code == 200
    assert response.json()["batch_size"] == 1
