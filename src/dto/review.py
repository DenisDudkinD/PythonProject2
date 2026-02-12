from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class ReviewCreate(BaseModel):
    review_id: UUID
    movie_id: UUID
    reviewer_name: str
    score: int
    created_at: datetime
    review_text: str


class ReviewRead(BaseModel):
    review_id: UUID
    movie_id: UUID
    reviewer_name: str
    score: int
    created_at: datetime
    review_text: str

    class Config:
        from_attributes = True
