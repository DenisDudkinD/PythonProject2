from src.domain.studio import Studio
from src.repositories.studio_repository_protocol import StudioRepositoryProtocol


class StudioService:
    def __init__(self, repo: StudioRepositoryProtocol):
        self.repo = repo

    def get_all_studios(self) -> list[Studio]:
        return self.repo.get_all_studios()

    def add_studio(self, studio: Studio) -> str:
        if not isinstance(studio, Studio):
            raise TypeError("Expected Studio, got something else")
        return self.repo.add_studio(studio)

    def get_studio_by_name(self, query: str) -> list[Studio]:
        if not isinstance(query, str):
            raise TypeError("Expected str, got something else")
        return self.repo.get_studio_by_name(query.strip().title())

    def remove_studio_by_id(self, studio_id:str):
        if not isinstance(studio_id, str):
            raise TypeError("Expected str, got something else")
        self.repo.remove_studio_by_id(studio_id)

    def update_studio(self, studio_id:str, studio:Studio):
        if not isinstance(studio_id, str):
            raise TypeError("Expected str, got something else")
        if not isinstance(studio, Studio):
            raise TypeError("Expected Studio, got something else")
        self.repo.update_studio(studio_id, studio)
    
    def add_seed_records(self, studios: list[Studio]) -> None:
        self.repo.add_seed_records(studios)