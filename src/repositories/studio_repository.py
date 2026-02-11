from sqlalchemy.orm import Session
from src.domain.Studio import Studio
from src.repositories.studio_repository_protocol import StudioRepositoryProtocol

class StudioRepository(StudioRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session