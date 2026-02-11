from sqlalchemy.orm import Session
from src.domain.actor import Actor
from src.repositories.actor_repository_protocol import ActorRepositoryProtocol

class SQLActorRepository(ActorRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session


    def add_actor(self, actor:Actor) -> None:
        self.session.add(actor)
        self.session.commit()
        
    def get_all_actors(self) -> list[Actor]:
        return self.session.query(Actor).all()
    
    def get_actor_by_name(self,query:str):
        return self.session.query(Actor).filter(Actor.full_name == query).first()

    def remove_actor_by_id(self,actor_id:str)-> None:
        actor = self.session.get(Actor,actor_id)
        if actor is None:
            raise ValueError("Actor Not Found")
        self.session.delete(actor)
        self.session.commit()

    def update_actor(self,actor:Actor)-> None:
        self.session.merge(actor)
        self.session.commit()


