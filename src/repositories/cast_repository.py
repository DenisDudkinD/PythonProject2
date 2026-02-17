from sqlalchemy.orm import Session
from src.domain.cast import Cast
from src.domain.actor import Actor
from src.domain.movie import Movie
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
        return self.session.get(Cast,(movie_id, actor_id))

    def get_cast_by_movie(self,movie_id:str) -> list[tuple[Cast, Actor]]:
        rows = (
            self.session.query(Cast, Actor)
            .join(Actor, Cast.actor_id == Actor.actor_id)
            .filter(Cast.movie_id == movie_id)
            .order_by(Cast.billing_order.asc())
            .all()
        )
        return rows
    
    def get_cast_by_actor(self,actor_id:str) -> list[tuple[Cast, Actor]]:
        rows = (
            self.session.query(Cast, Movie)
            .join(Movie, Cast.movie_id == Movie.movie_id)
            .filter(Cast.actor_id == actor_id)
            .order_by(Cast.billing_order.asc())
            .all()
        )
        return rows
    
    def remove_cast(self,movie_id:str,actor_id:str) -> None:
        cast = self.session.get(Cast,(movie_id, actor_id))
        if cast is None:
            raise ValueError("Cast Not Found")
        self.session.delete(cast)
        self.session.commit()

    def update_cast(self,cast:Cast) -> None:
        self.session.merge(cast)
        self.session.commit()

    def add_seed_records(self, casts: list[Cast]) -> None:
        for c in casts:
            self.session.add(c)
        self.session.commit()