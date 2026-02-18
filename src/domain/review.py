import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.base import Base
from sqlalchemy.orm import relationship

class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    movie_id = Column(UUID(as_uuid=True),ForeignKey("movies.movie_id"), nullable=False)

    reviewer_name = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    review_text = Column(String, nullable=False)

    movie = relationship("Movie", backref="reviews")
