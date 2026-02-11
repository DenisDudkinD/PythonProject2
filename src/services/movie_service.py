from src.repositories.movie_repository_protocol import MovieRepositoryProtocol
from src.domain.movie import Movie

class MovieService:
    def __init__(self, repo: MovieRepositoryProtocol):
        self.repo = repo
    
    def add_movie(self, movie: Movie) -> str:
        if not isinstance(movie, Movie):
            raise TypeError("Expected Movie, got something else.")
        return self.repo.add_movie(movie)
    
    def get_all_movies(self) -> list[Movie]:
        return self.repo.get_all_movies()
    
    def find_movies_by_title(self, query: str) -> list[Movie]:
        if not isinstance(query, str):
            raise TypeError("Expected str, got something else.")
        if not query.strip():
            raise ValueError("Query cannot be empty.")
        return self.repo.find_movies_by_title(query)
    
    def remove_movie(self, movie_id: str) -> None:
        if not isinstance(movie_id, str):
            raise TypeError("Expected str, got something else")
        return self.repo.remove_movie(movie_id)
    
    def update_movie(self, movie: Movie) -> None:
        if not isinstance(movie, Movie):
            raise TypeError("Expected Movie, got something else")
        return self.repo.update_movie(movie)