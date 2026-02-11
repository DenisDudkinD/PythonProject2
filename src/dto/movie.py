from typing import Optional
from uuid import UUID
from datetime import date
from pydantic import BaseModel


class MovieCreate(BaseModel):
    studio_id: UUID
    title: str
    released_date: Optional[date] = None
    runtime_minutes: Optional[int] = None
    rating: Optional[str] = None
    sequel_to_movie_id: Optional[UUID] = None


class MovieRead(MovieCreate):
    movie_id: UUID

    class Config:
        from_attributes = True
        fields = {
            "movie_id": ...,
            "title": ...,
            "studio_id": ...,
        }