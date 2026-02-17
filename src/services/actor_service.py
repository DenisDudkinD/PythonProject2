from multiprocessing import Value
from src.domain.actor import Actor
from src.domain.exceptions import NotFoundException
from src.repositories.actor_repository import ActorRepositoryProtocol
import uuid

class ActorService:
    def __init__(self, repo: ActorRepositoryProtocol):
        self.repo = repo

    def get_all_actors(self) -> list[Actor]:
        return self.repo.get_all_actors()
    
    def get_actor_by_id(self, actor_id:str)->Actor:
        try:
            uuid.UUID(actor_id)
        except(ValueError) as e:
            raise ValueError("Invalid ID format") from e
        actor = self.repo.get_actor_by_id(actor_id)
        if actor is None:
            raise NotFoundException(f"Actor not Found. ID: {actor_id}")
        return actor


    def add_actor(self, actor:Actor) -> str:
        if not isinstance(actor, Actor):
            raise TypeError("Expected actor, got something else")
        return self.repo.add_actor(actor)

    def get_actor_by_name(self, query: str) -> list[Actor]:
        if not isinstance(query, str):
            raise TypeError("Expected str, got something else")
        return self.repo.get_actor_by_name(query)

    def remove_actor_by_id(self, actor_id:str):
        try:
            uuid.UUID(actor_id)
        except(ValueError) as e:
            raise ValueError("Invalid ID format") from e
        actor = self.repo.get_actor_by_id(actor_id)
        if actor is None:
            raise NotFoundException(f"Actor not Found. ID: {actor_id}")
        self.repo.remove_actor_by_id(actor_id)

    def update_actor(self, actor:Actor):
        if not isinstance(actor, Actor):
            raise TypeError("Expected actor, got something else")
        try:
            uuid.UUID(actor.actor_id)
        except(ValueError) as e:
            raise ValueError("Invalid ID format") from e
        actor_temp = self.repo.get_actor_by_id(actor.actor_id)
        if actor_temp is None:
            raise NotFoundException(f"Actor not Found. ID: {actor_temp.actor_id}")
        self.repo.update_actor(actor)

    def add_seed_records(self, actors: list[Actor]) -> None:
        self.repo.add_seed_records(actors)