from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from database import db

router=APIRouter(prefix="/users", tags=["users"])

class User(BaseModel):
    name:str
    email:EmailStr
    phone:str

@router.get("/")
def get_users():
    users =list(db.users.find({},{"id_":0}))
    return users

#get a specific user detaul by email
@router.get("/{email}")
def get_user(email:str):
    user=db.users.find_one({"email": email} , {"_id":0})
    if not user:
        raise HTTPException(status_code=404 , detail="User not found")
    return user

#update user details
@router.put("/{email}")
def update_user(email:str , user:User):
    existing_user=db.users.find_one({"email":email})
    if not existing_user:
        raise HTTPException(status_code=404 , detail="User not found")
    db.users.update_one({"email":email} , {"$set":user.dict(exclude_unset=True)})
    return {"message": "Use updated successfully"}

#delete a user by email
@router.delete("/{email}")
def delete_user(email:str):
    result=db.users.delete_one({"email": email})
    if result.deleted_count==0:
        raise HTTPException(status_code=404 , detail="User not found")
    return {"message": "User deleted successfully"}


