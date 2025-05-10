import os
import pytest
from fastapi.testclient import TestClient

# برای اجرای تست به جای "db" از "localhost" استفاده می‌کنیم
os.environ["DATABASE_URL"] = "localhost+asyncpg://AmirRzn:Amir1380@localhost:5432/tasks_db"

from app.main import app

client = TestClient(app)

@pytest.fixture
def login_user():
    response = client.post("/auth/login", json={"username": "Amir", "password": "1111"})
    print("Login response:", response.json())
    assert response.status_code == 200
    token = response.json().get("access_token")
    return token

def test_login():
    response = client.post("/auth/login", json={"username": "Amir", "password": "1111"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task_with_auth(login_user):
    headers = {"Authorization": f"Bearer {login_user}"}
    response = client.post("/tasks/", json={"title": "Secure Task", "description": "With Auth"}, headers=headers)
    assert response.status_code == 201
