from __future__ import annotations

from typing import Dict
from src.domain.movie import Movie
from src.repositories.movie_repository_protocol import MovieRepositoryProtocol


class MockMovieRepo(MovieRepositoryProtocol):
    def __init__(self):
        self._movies: Dict[str, Movie] = {}

        seed = Movie(
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
        self._movies[str(seed.movie_id)] = seed

    def get_all_movies(self) -> list[Movie]:
        return list(self._movies.values())

    def add_movie(self, movie: Movie) -> str:
        movie_id = str(movie.movie_id)
        self._movies[movie_id] = movie
        return movie_id

    def find_movies_by_title(self, query: str) -> list[Movie]:
        q = query.strip().lower()
        return [m for m in self._movies.values() if (m.title or "").strip().lower() == q]

    def get_movie_by_id(self, movie_id: str) -> Movie | None:
        return self._movies.get(str(movie_id))   # <-- fixed

    def remove_movie(self, movie_id: str) -> None:
        movie_id = str(movie_id)
        if movie_id not in self._movies:
            raise ValueError("Movie not found")
        del self._movies[movie_id]

    def update_movie(self, movie: Movie) -> None:
        movie_id = str(movie.movie_id)
        if movie_id not in self._movies:
            raise ValueError("Movie not found")
        self._movies[movie_id] = movie

    def add_seed_records(self, movies: list[Movie]) -> None:
        pass