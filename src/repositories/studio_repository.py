from sqlalchemy.orm import Session
from src.domain.studio import Studio
from src.repositories.studio_repository_protocol import StudioRepositoryProtocol

class StudioRepository(StudioRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session

    def add_studio(self, studio:Studio) -> str:
        self.session.add(studio)
        self.session.commit()
        return str(studio.studio_id)


    def get_all_studios(self) -> list[Studio]:
        return self.session.query(Studio).all()

    def get_studio_by_name(self,query:str) -> list[Studio]:
        return self.session.query(Studio).filter(Studio.name == query).all()
        
    def remove_studio_by_id(self,studio_id:str):
        studio = self.session.get(Studio, studio_id)
        self.session.delete(studio)
        self.session.commit()

    def update_studio(self,studio_id:str,studio:Studio):
        self.remove_studio_by_id(studio_id)
        self.add_studio(studio)