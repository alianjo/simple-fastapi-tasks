from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
<<<<<<< HEAD
    username: str  
=======
    username: str

class TaskOut(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True  
>>>>>>> 5a4d977 (Updated README and finalized project)
