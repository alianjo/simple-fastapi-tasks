from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
<<<<<<< HEAD
from models.task import Task as TaskModel  # مدل تسک از SQLAlchemy را وارد می‌کنیم
from pydantic import BaseModel
from fastapi import Depends

# مدل داده‌ای برای تسک‌ها
=======
from models.task import Task as TaskModel
from pydantic import BaseModel
from fastapi import Depends
from sqlalchemy.future import select
from models.models import TaskOut

>>>>>>> 5a4d977 (Updated README and finalized project)
class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True

class Task(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True

router = APIRouter()

@router.post("/", response_model=Task)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    db_task = TaskModel(title=task.title, description=task.description)
    db.add(db_task)
<<<<<<< HEAD
=======
    await db.commit() 
    await db.refresh(db_task)  
    return db_task

@router.get("/", response_model=list[TaskOut])  
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TaskModel))  
    tasks = result.scalars().all()
    return tasks

@router.get("/{task_id}", response_model=TaskOut)  
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TaskModel).filter(TaskModel.id == task_id))
    task = result.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TaskModel).filter(TaskModel.id == task_id))  
    db_task = result.scalars().first()  
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
>>>>>>> 5a4d977 (Updated README and finalized project)
    await db.commit()  
    await db.refresh(db_task)  
    return db_task

<<<<<<< HEAD
@router.get("/", response_model=list[Task])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(TaskModel.__table__.select()) 
    tasks = result.scalars().all()
    return tasks

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await db.execute(TaskModel.__table__.select().filter(TaskModel.id == task_id))  
    task = task.scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    db_task = await db.execute(TaskModel.__table__.select().filter(TaskModel.id == task_id))  
    db_task = db_task.scalars().first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.title = task.title
    db_task.description = task.description
    await db.commit()  
    await db.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await db.execute(TaskModel.__table__.select().filter(TaskModel.id == task_id)) 
    db_task = db_task.scalars().first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    await db.delete(db_task)  
    await db.commit()
    return {"message": "Task deleted successfully"}  
=======

@router.delete("/{task_id}")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TaskModel).filter(TaskModel.id == task_id))  
    db_task = result.scalars().first()  
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    await db.delete(db_task)  
    await db.commit()  
    return {"message": "Task deleted successfully"}
>>>>>>> 5a4d977 (Updated README and finalized project)
