from fastapi import APIRouter , HTTPException , Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from database import db

router=APIRouter(prefix="/auth",tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    name:str
    email:str
    password:str

@router.post("/register")
def register(user:User):
    existing_user=db.users.find_one({"email":user.email})
    if existing_user:
        raise HTTPException(status_code=400 , detail="email already exists")
    hashed_pasword=pwd_context.hash(user.password)
    db.users.insert_one({"name":user.name , "email":user.email ,"password":user.password })
    return {"message":"user registered successfully"}

@router.post("/login")
def login(user:User):
    existing_user=db.users.find_one({"email":user.email})
    if not existing_user or not pwd_context.verify(user.password , existing_user["password"]):
        raise HTTPException(status_code=401 , detail="invalid credentials")
    return {"message":"Login successfull"}
    