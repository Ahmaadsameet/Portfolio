from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_create_task():
    response = client.post("/tasks", json={
        "id": 1,
        "title": "Learn DevOps",
        "completed": False
    })
    assert response.status_code == 200