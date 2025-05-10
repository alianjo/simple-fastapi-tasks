from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.auth import create_access_token, verify_token
from models import UserIn, UserOut

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.post("/token", response_model=UserOut)
def login(user: UserIn):
    if user.username == "testuser" and user.password == "testpassword":
        access_token = create_access_token(data={"sub": user.username})
        return {"username": user.username, "access_token": access_token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/verify")
def verify(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"message": "Token is valid", "user": payload} 
