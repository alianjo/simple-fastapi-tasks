from fastapi import FastAPI
from routes.task import router as task_router
from app.auth import router as auth_router
from app.database import create_tables

app = FastAPI()

app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}  

@app.on_event("startup")
async def startup():
    await create_tables()
