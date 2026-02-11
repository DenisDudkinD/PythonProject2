from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.base import Base

class Cast(Base):
    __tablename__ = "movie_cast"

    movie_id= Column(UUID(as_uuid=True), ForeignKey("movies.movie_id"), primary_key=True)

    actor_id = Column(UUID(as_uuid=True),ForeignKey("actors.actor_id"), primary_key=True)

    role_type = Column(String, nullable=False)
    character_name = Column(String, nullable=False)
    billing_order = Column(Integer,nullable=False)

