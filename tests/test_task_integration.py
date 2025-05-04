import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db, SessionLocal
from models.task import Task
from routes.task import TaskCreate, TaskUpdate

client = TestClient(app)

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def create_task():
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "Test Description"},
    )
    return response.json()

def test_create_task():
    response = client.post(
        "/tasks/",
        json={"title": "New Task", "description": "Task Description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Task"
    assert data["description"] == "Task Description"

def test_get_tasks(create_task):
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) > 0

def test_get_task(create_task):
    task_id = create_task["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == create_task["title"]

def test_update_task(create_task):
    task_id = create_task["id"]
    updated_data = {"title": "Updated Task", "description": "Updated Description"}
    response = client.put(f"/tasks/{task_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

def test_delete_task(create_task):
    task_id = create_task["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"
