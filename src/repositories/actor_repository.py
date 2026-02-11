from sqlalchemy.orm import Session
from src.domain.actor import Actor
from src.repositories.actor_repository_protocol import ActorRepositoryProtocol

class SQLActorRepository(ActorRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session


    def add_actor(self, actor:Actor):
        self.session.add(actor)
        self.session.commit()

    def get_all_actors(self) -> list[Actor]:
        return self.session.query(Actor).all()
    
    def get_actor_by_name(self,query:str):
        return self.session.query(Actor).filter(Actor.full_name == query).all()

    def remove_actor(self,actor:Actor):
        self.session.delete(actor)
        self.session.commit()

    def update_actor(self,actor:Actor):
        self.session.merge(actor)
        self.session.commit()