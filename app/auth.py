from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db

router = APIRouter()

<<<<<<< HEAD
SECRET_KEY = "example"
=======
SECRET_KEY = "your secret key"
>>>>>>> 5a4d977 (Updated README and finalized project)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {}

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

<<<<<<< HEAD

=======
>>>>>>> 5a4d977 (Updated README and finalized project)
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = pwd_context.hash(user.password)
    fake_users_db[user.username] = hashed_password
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    if user.username not in fake_users_db:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    hashed_password = fake_users_db[user.username]
    print(f"Stored hash: {hashed_password}")
    
    if not pwd_context.verify(user.password, hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}  