import uuid
from datetime import date
from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
from src.base import Base

class Actor(Base):
    __tablename__ = "actors"

    actor_id= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    full_name = Column(String, nullable=False)
    birth_date = Column(Date, default=date.today())
    nationality = Column(String, nullable=False)


