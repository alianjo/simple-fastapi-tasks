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

# Task Management API

A FastAPI-based Task Management API with full CRUD functionality, JWT authentication, PostgreSQL database, and Docker support.

## Features

- User authentication using JWT (Login/Register)
- Task management (Create, Read, Update, Delete)
- Asynchronous database operations with SQLAlchemy and asyncpg
- PostgreSQL as the database
- Docker and Docker Compose for easy deployment
- Pydantic models for request validation
- Auto-generated interactive API documentation using Swagger UI

## Setup

### Local Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/task-management-api.git
   cd task-management-api
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```sh
   uvicorn app.main:app --reload
   ```
5. **Visit the API docs:**
   - Open `http://127.0.0.1:8000/docs` in your browser.

### Using Docker

1. **Build and start the containers:**
   ```sh
   docker-compose up --build
   ```
2. **The API will be available at:** `http://localhost:8000`

## API Endpoints

### Authentication

- **Signup:** `POST /auth/signup/` `{ "username": "user", "password": "pass" }`
- **Login:** `POST /auth/login/` `{ "username": "user", "password": "pass" }`

### Tasks (Requires Authentication)

- **Create Task:** `POST /tasks/` `{ "title": "Task", "description": "Details" }`
- **Get All Tasks:** `GET /tasks/`
- **Get Task by ID:** `GET /tasks/{task_id}`
- **Update Task:** `PUT /tasks/{task_id}` `{ "title": "Updated", "description": "New details" }`
- **Delete Task:** `DELETE /tasks/{task_id}`

## Database

- Uses **PostgreSQL** for data storage.
- Async database operations with `SQLAlchemy` and `asyncpg`.

## Deployment

- The project is containerized using **Docker**.
- Use `docker-compose` to deploy easily.
- Configure environment variables in `.env` file.

## Future Improvements

- Role-based access control (RBAC)
- Unit and integration testing
- CI/CD pipeline integration