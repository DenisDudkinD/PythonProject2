import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.base import Base

class Movie(Base):
    __tablename__ = "movies"

    movie_id= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    studio_id = Column(UUID(as_uuid=True),ForeignKey("studios.studio_id"), nullable=False)

    title = Column(String, nullable=False)
    released_date = Column(DateTime, default=datetime.now(timezone.utc))
    runtime_minutes = Column(Integer, nullable=True)
    rating = Column(String, nullable=True)

    sequel_to_movie_id = Column(UUID(as_uuid=True),ForeignKey("movies.movie_id"), nullable=True)

