from src.domain.movie import Movie
from src.repositories.movie_repository_protocol import MovieRepositoryProtocol

class MockMovieRepo(MovieRepositoryProtocol):
    def get_all_movies(self) -> list[Movie]:
        return [
            Movie(
                movie_id="mock_id",
                studio_id="studio_1",
                title="Mock Movie",
                release_date=None,
                runtime_minutes=120,
                rating="PG",
                production_cost=100000,
                revenue=500000,
                sequel_to_movie_id=None,
            )
        ]
    
    def add_movie(self, movie: Movie) -> str:
        return "mock_id"

    def find_movies_by_title(self, query: str) -> list[Movie]:
        return [
            Movie(
                movie_id="mock_id",
                studio_id="studio_1",
                title=query,
                release_date=None,
                runtime_minutes=120,
                rating="PG",
                production_cost=100000,
                revenue=500000,
                sequel_to_movie_id=None,
            )
        ]
    
    def get_movie_by_id(self, movie_id: str) -> Movie | None:
        if movie_id != "mock_id":
            return None

        return Movie(
            movie_id="mock_id",
            studio_id="studio_1",
            title="Mock Movie",
            release_date=None,
            runtime_minutes=120,
            rating="PG",
            production_cost=100000,
            revenue=500000,
            sequel_to_movie_id=None,
        )
    
    def remove_movie(self, movie_id: str) -> None:
        if movie_id != "mock_id":
            raise ValueError("Movie not found")
        

    def update_movie(self, movie: Movie) -> None:
        if movie.movie_id != "mock_id":
            raise ValueError("Movie not found")

    def add_seed_records(self, movies):
        pass