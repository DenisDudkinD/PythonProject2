from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import date

class ActorCreate(BaseModel):
    full_name: str
    birth_date: Optional[date] = None
    nationality: Optional[str] = None

class ActorRead(BaseModel):
    actor_id: UUID
    full_name: str
    birth_date: Optional[date]
    nationality: Optional[str] = None

    class Config:
        from_attributes = True