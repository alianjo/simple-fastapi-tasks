from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD
from app.database import get_db
=======
from app.database import get_db  
>>>>>>> 5a4d977 (Updated README and finalized project)

async def get_db_session(db: AsyncSession = Depends(get_db)):
    try:
        yield db
    finally:
<<<<<<< HEAD
        await db.close()
=======
        await db.close() 
>>>>>>> 5a4d977 (Updated README and finalized project)
