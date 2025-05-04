from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

class TaskOut(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True  
