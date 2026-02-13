from sqlalchemy.orm import Session
from sqlalchemy import func

from src.domain.movie import Movie
from src.repositories.movie_repository_protocol import MovieRepositoryProtocol

class MovieRepository(MovieRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session
    
    def add_movie(self, movie: Movie):
        self.session.add(movie)
        self.session.commit()
        return str(movie.movie_id)
    
    def get_all_movies(self) -> list[Movie]:
        return  self.session.query(Movie).all()
    
    def find_movies_by_title(self, query: str) -> list[Movie]:
        return self.session.query(Movie).filter(func.lower(Movie.title) == query.lower()).all()
    
    def remove_movie(self, movie_id: str):
        movie = self.session.get(Movie, movie_id)
        if movie is None:
            raise ValueError(f"Movie with id {movie_id} not found.")
        self.session.delete(movie)
        self.session.commit()

    def update_movie(self, movie: Movie) -> None:
        self.session.merge(movie)
        self.session.commit()

    def get_movie_by_id(self, movie_id: str) -> Movie | None:
        return self.session.get(Movie, movie_id)

    def add_seed_records(self, movies: list[Movie]) -> None:
        for m in movies:
            self.session.add(m)
        self.session.commit()