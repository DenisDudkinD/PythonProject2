from src.domain.studio import Studio
from src.repositories.studio_repository_protocol import StudioRepositoryProtocol


class MockStudioRepo(StudioRepositoryProtocol):
    def get_all_studios(self):
        return [Studio(name="Test Studio", country="USA")]

    def add_studio(self, studio):
        return "mock_id"

    def get_studio_by_id(self, studio_id):
        return [Studio(name="Test Studio", country="USA")]

    def get_studio_by_name(self, query):
        return [Studio(name="Test Studio", country="USA")]

    def remove_studio_by_id(self, studio_id):
        pass

    def update_studio(self, studio_id, studio):
        pass

    def add_seed_records(self, studios):
        pass
