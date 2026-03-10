from fastapi import FastAPI

from app.database import Base, engine
from app.models import User, Task

from app.routers import auth
from app.routers import tasks


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Task Manager API is working!"}  