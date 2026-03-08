from pydantic import BaseModel
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    
    
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True