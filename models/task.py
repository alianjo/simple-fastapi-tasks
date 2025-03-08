from sqlalchemy import Column, Integer, String
<<<<<<< HEAD
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
=======
from app.database import Base  
>>>>>>> 5a4d977 (Updated README and finalized project)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
<<<<<<< HEAD
    description = Column(String) 
=======
    description = Column(String)
>>>>>>> 5a4d977 (Updated README and finalized project)
