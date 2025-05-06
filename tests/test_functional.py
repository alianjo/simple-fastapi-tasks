import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def signup_user():
    response = client.post("/auth/signup", json={"username": "testuser", "password": "testpassword"})
    return response.json()

@pytest.fixture
def login_user(signup_user):
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpassword"})
    return response.json()["access_token"]

def test_signup():
    response = client.post("/auth/signup", json={"username": "newuser", "password": "newpassword"})
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"

def test_login():
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task_with_auth(login_user):
    headers = {"Authorization": f"Bearer {login_user}"}
    response = client.post("/tasks/", json={"title": "Secure Task", "description": "With Auth"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Secure Task"

def test_delete_task_with_auth(login_user):
    headers = {"Authorization": f"Bearer {login_user}"}
    response = client.post("/tasks/", json={"title": "Task To Delete", "description": "Delete me"}, headers=headers)
    task_id = response.json()["id"]
    response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"
