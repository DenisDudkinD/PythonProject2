from sqlalchemy.orm import Session
from src.domain.actor import Actor
from src.repositories.actor_repository_protocol import ActorRepositoryProtocol

class SQLBookRepository(ActorRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session