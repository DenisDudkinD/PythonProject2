from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class StudioCreate(BaseModel):
    name: str
    country: str
    founded_year: Optional[int] = None


class StudioRead(StudioCreate):
    studio_id: UUID
    name: str
    country: str

    class Config:
        from_attributes = True
        fields = {
            "studio_id": ...,
            "title": ...,
            "author": ...,
        }
