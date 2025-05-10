from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://AmirRzn:Amir1380@localhost:5432/tasks_db"
engine = create_async_engine(DATABASE_URL)

async def test_connection():
    async with engine.begin() as conn:
        print("Connected successfully!")

import asyncio
asyncio.run(test_connection())
