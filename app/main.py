from fastapi import FastAPI
from routes.task import router as task_router
from app.auth import router as auth_router
<<<<<<< HEAD
=======
from app.database import create_tables
>>>>>>> 5a4d977 (Updated README and finalized project)

app = FastAPI()

app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager API"}  
<<<<<<< HEAD
=======

@app.on_event("startup")
async def startup():
    await create_tables()
>>>>>>> 5a4d977 (Updated README and finalized project)
