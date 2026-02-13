from uuid import UUID
from pydantic import BaseModel

class CastCreate(BaseModel):
    movie_id: UUID
    actor_id: UUID
    role_type: str
    character_name: str
    billing_order:int

class CastRead(BaseModel):
    movie_id: UUID
    actor_id: UUID
    role_type: str
    character_name: str
    billing_order:int

    class Config:
        from_attributes = True

class MovieCastRead(BaseModel):
    movie_id: UUID
    actor_id: UUID
    actor_name: str
    role_type: str
    character_name: str
    billing_order: int
