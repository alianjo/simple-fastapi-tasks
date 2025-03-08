from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

<<<<<<< HEAD
DATABASE_URL = "postgresql+asyncpg://AmirRzn:Amir1380@db:5432/tasks_db"  
=======
DATABASE_URL = "postgresql+asyncpg://AmirRzn:Amir1380@db:5432/tasks_db"

Base = declarative_base()
>>>>>>> 5a4d977 (Updated README and finalized project)

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

<<<<<<< HEAD
Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:  
        yield db 
=======
async def get_db():
    async with SessionLocal() as db:  
        yield db  

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
>>>>>>> 5a4d977 (Updated README and finalized project)
