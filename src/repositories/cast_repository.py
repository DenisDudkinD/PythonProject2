from sqlalchemy.orm import Session
from src.domain.cast import Cast
from src.repositories.cast_repository_protocol import CastRepositoryProtocol

class SQLCastRepository(CastRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session

    def add_cast(self, cast:Cast) -> None:
        self.session.add(cast)
        self.session.commit()

    def get_all_casts(self) -> list[Cast]:
        return self.session.query(Cast).all()
    
    def get_specific_cast(self,movie_id:str,actor_id:str)->Cast:
        return self.session.query(Cast).filter(Cast.movie_id == movie_id,Cast.actor_id == actor_id).one_or_none()

    def get_cast_by_movie(self,movie_id:str)-> list[Cast]:
        return self.session.query(Cast).filter(Cast.movie_id == movie_id).all()
    
    def remove_cast(self,cast:Cast) -> None:
        self.session.delete(cast)
        self.session.commit()

    def update_cast(self,cast:Cast) -> None:
        self.session.merge(cast)
        self.session.commit()

