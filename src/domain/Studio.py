import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from src.base import Base


class Studio(Base):
    __tablename__ = "studios"

    studio_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
 
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    founded_year = Column(Integer, nullable=True)
