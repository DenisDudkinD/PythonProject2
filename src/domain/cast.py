from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.base import Base
from sqlalchemy.orm import relationship

class Cast(Base):
    __tablename__ = "movie_cast"

    movie_id= Column(UUID(as_uuid=True), ForeignKey("movies.movie_id",ondelete="CASCADE"), primary_key=True)
    actor_id = Column(UUID(as_uuid=True),ForeignKey("actors.actor_id",ondelete="CASCADE"), primary_key=True)

    role_type = Column(String, nullable=False)
    character_name = Column(String, nullable=False)
    billing_order = Column(Integer,nullable=False)

    movie = relationship("Movie", backref="cast_members")
    actor = relationship("Actor", backref="cast_roles")
