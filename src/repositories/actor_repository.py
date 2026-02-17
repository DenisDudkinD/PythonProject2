from sqlalchemy.orm import Session
from src.domain.actor import Actor
from src.repositories.actor_repository_protocol import ActorRepositoryProtocol

class SQLActorRepository(ActorRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session


    def add_actor(self, actor:Actor) -> str:
        self.session.add(actor)
        self.session.commit()
        return str(actor.actor_id)
        
    def get_all_actors(self) -> list[Actor]:
        return self.session.query(Actor).all()
    
    def get_actor_by_name(self,query:str) -> list[Actor]:
        return self.session.query(Actor).filter(Actor.full_name == query).all()

    def get_actor_by_id(self,actor_id:str)-> Actor:
        return self.session.get(Actor,actor_id)

    def remove_actor_by_id(self,actor_id:str)-> str:
        actor = self.session.get(Actor,actor_id)
        if actor is None:
            raise ValueError("Actor Not Found")
        self.session.delete(actor)
        self.session.commit()
        return actor.actor_id

    def update_actor(self,actor:Actor)-> str:
        updated_actor = self.session.merge(actor)
        self.session.commit()
        return updated_actor.actor_id
    
    def add_seed_records(self, actors: list[Actor]) -> None:
        for a in actors:
            self.session.add(a)
        self.session.commit()
