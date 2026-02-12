from src.domain.cast import Cast
from src.repositories.actor_repository import ActorRepositoryProtocol

class StudioService:
    def __init__(self, repo: ActorRepositoryProtocol):
        self.repo = repo

    def get_all_casts(self) -> list[Cast]:
        return self.repo.get_all_casts()

    def add_cast(self, cast:Cast) -> str:
        if not isinstance(cast, cast):
            raise TypeError("Expected cast, got something else")
        return self.repo.add_cast(cast)

    def get_cast(self, movie_id:str,actor_id:str):
        return self.repo.get_specific_cast(movie_id,actor_id)

    def get_cast_by_movie(self, movie_id:str):
        return self.repo.get_cast_by_movie(movie_id)
    
    def remove_cast(self, movie_id:str,actor_id:str):
        self.repo.remove(movie_id,actor_id)

    def update_cast(self, cast:Cast):
        if not isinstance(cast, cast):
            raise TypeError("Expected cast, got something else")
        self.repo.update_cast(cast)
    
    def add_seed_records(self, casts: list[Cast]) -> None:
        self.repo.add_seed_records(casts)