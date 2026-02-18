from src.domain.cast import Cast
from src.domain.exceptions import NotFoundException
from src.repositories.cast_repository_protocol import CastRepositoryProtocol
import uuid

class CastService:
    def __init__(self, repo: CastRepositoryProtocol):
        self.repo = repo

    def get_all_casts(self) -> list[Cast]:
        return self.repo.get_all_casts()

    def add_cast(self, cast: Cast) -> None:
        if not isinstance(cast, Cast):
            raise TypeError("Expected cast, got something else")
        self.repo.add_cast(cast)

    
    def get_cast(self,movie_id : str = None, actor_id:str = None) -> list[Cast]:
        if movie_id and actor_id:
            try:
                 uuid.UUID(actor_id)
                 uuid.UUID(movie_id)
                 cast = self.repo.get_specific_cast(movie_id,actor_id)
                 if cast is None:
                     raise (NotFoundException("Cast Not Found"))
                 return [cast]
            except(ValueError) as e:
               raise ValueError("Invalid ID format") from e
        else:
            return self.repo.get_all_casts()

    def get_cast_by_movie(self, movie_id: str):
        try:
            uuid.UUID(movie_id)
        except(ValueError) as e:
            raise ValueError("Invalid ID format") from e
        if not isinstance(movie_id, str):
            raise TypeError("Expected str, got something else.")
        return self.repo.get_cast_by_movie(movie_id)

    def get_cast_by_actor(self, actor_id: str):
        try:
            uuid.UUID(actor_id)
        except(ValueError) as e:
            raise ValueError("Invalid ID format") from e
        if not isinstance(actor_id, str):
            raise TypeError("Expected str, got something else.")
        return self.repo.get_cast_by_actor(actor_id)
    
    def remove_cast(self, movie_id: str, actor_id: str):
        try:
            uuid.UUID(actor_id)
            uuid.UUID(movie_id)
        except(ValueError) as e:
            raise ValueError("Invalid ID format") from e
        cast = self.repo.get_specific_cast(movie_id,actor_id)
        if cast is None:
            raise NotFoundException('Cast Not Found')
        self.repo.remove_cast(movie_id, actor_id)

    def update_cast(self, cast: Cast):
        try:
            uuid.UUID(cast.actor_id)
            uuid.UUID(cast.movie_id)
        except(ValueError) as e:
            raise ValueError("Invalid ID format") from e
        if not isinstance(cast, Cast):
            raise TypeError("Expected cast, got something else")
        self.repo.update_cast(cast)

    def add_seed_records(self, casts: list[Cast]) -> None:
        self.repo.add_seed_records(casts)
