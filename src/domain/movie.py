import uuid
from datetime import date
from sqlalchemy import CheckConstraint, Column, String, Date, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.base import Base

class Movie(Base):
    __tablename__ = "movies"

    __table_args__ = (
        CheckConstraint("production_cost >= 0", name="check_production_cost_positive"),
    )

    movie_id= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    studio_id = Column(UUID(as_uuid=True),ForeignKey("studios.studio_id"), nullable=False)

    title = Column(String(200), nullable=False)
    release_date = Column(Date, default=date.today)
    runtime_minutes = Column(Integer, nullable=True)
    rating = Column(String(10), nullable=True)
    production_cost= Column(Integer, nullable = True)
    revenue= Column(Integer, nullable = True)

    sequel_to_movie_id = Column(UUID(as_uuid=True),ForeignKey("movies.movie_id"), nullable=True)

