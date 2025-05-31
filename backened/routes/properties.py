from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from database import db

router=APIRouter(prefix="/properties" , tags=["properties"])

class Property(BaseModel):
    title:str
    description:str
    price:str
    location:str
    owner_email:str

@router.post("/add")
def add_property(property:Property):
    existing_property=db.properties.find_one({"title":property.title})
    if existing_property:
        raise HTTPException(status_code=400 , detail="Property with this title  already exists")
    db.properties.insert_one(property.dict())
    return {"message": "Property added successfully"}
@router.get("/")
def get_properties():
    properties=list(db.properties.find({},{"_id":0}))
    return properties

@router.get("/{title}")
def get_property(title:str):
    property= db.properties.find_one({"title":title} , {"_id":0})
    if not property:
        raise HTTPException(status_code=404 , detail="Property is not found")
    return property

@router.delete("/{title}")
def delete_property(title:str):
    result=db.properties.delete_one({"title":title})
    if result.deleted_count==0:
        raise HTTPException(status_code=404 ,detail="Property not found")
    return {"message":"property deleted successfully"}
   