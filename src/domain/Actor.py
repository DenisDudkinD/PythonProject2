import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.base import Base

class Actor(Base):
    __tablename__ = "actors"

    actor_id= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    full_name = Column(String, nullable=False)
    birth_date = Column(DateTime, default=datetime.now(timezone.utc))
    nationality = Column(String, nullable=False)


