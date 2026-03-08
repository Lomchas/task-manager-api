from fastapi import FastAPI
from app.database import Base, engine
from app.models import User, Task

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Task Manager API is working!"}  