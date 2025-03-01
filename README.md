# Task Management API

A simple FastAPI project to learn CRUD operations for managing tasks, with plans to add database and authentication.

## Features
- Create, read, update, delete tasks
- Planned: SQLite (start), PostgreSQL (later), JWT auth

## Setup
1. Clone: `git clone https://github.com/your-username/task-management-api.git`
2. Virtual env: `python -m venv venv && source venv/bin/activate`
3. Install: `pip install fastapi uvicorn sqlalchemy databases`
4. Run: `uvicorn main:app --reload`
5. Visit: `http://127.0.0.1:8000/docs`

## Usage
- POST `/tasks/`: `{ "title": "Task", "description": "Details" }`
- GET `/tasks/`, GET `/tasks/{id}`, PUT `/tasks/{id}`, DELETE `/tasks/{id}`

## Database
- SQLite: Simple, file-based (start here)
- PostgreSQL: Scalable, production-ready (upgrade later)

## Learning
- Start with list-based CRUD
- Add Pydantic, SQLite, then PostgreSQL, and auth
- Add docker-compose.yml file and Dockerfile
