from fastapi import FastAPI
from routes import auth , properties , users
app=FastAPI()
app.include_router(auth.router)
app.include_router(properties.router)
app.include_router(users.router)
@app.get("/")
def home():
    return {"message":"welcome"}
