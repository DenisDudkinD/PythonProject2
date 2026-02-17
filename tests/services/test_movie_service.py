import pytest

from src.services.movie_service import MovieService
from src.domain.movie import Movie
from tests.mocks.mock_movie_repository import MockMovieRepo

def make_movie(**overrides):
    data = dict(
        movie_id="new_movie_id",
        studio_id="studio_mock_id",
        title="Some Title",
        release_date=None,
        runtime_minutes=100,
        rating="PG",
        sequel_to_movie_id=None,
        production_cost=100000,
        revenue=200000,
    )
    data.update(overrides)
    return Movie(**data)

def test_add_movie_returns_id():
    svc = MovieService(MockMovieRepo())
    movie = make_movie(movie_id="abc123")
    movie_id = svc.add_movie(movie)

    assert movie_id == "abc123"

def test_add_movie_type_check():
    svc = MovieService(MockMovieRepo())

    with pytest.raises(TypeError):
        svc.add_movie("not a movie")

def test_get_all_movies_returns_list():
    svc = MovieService(MockMovieRepo())
    movies = svc.get_all_movies()

    assert isinstance(movies, list)
    assert len(movies) >= 1

def test_find_movies_by_title_positive():
    svc = MovieService(MockMovieRepo())
    results = svc.find_movies_by_title("Mock Movie")

    assert len(results) == 1
    assert results[0].title == "Mock Movie"

def test_find_movies_by_title_negative():
    svc = MovieService(MockMovieRepo())

    with pytest.raises(ValueError):
        svc.find_movies_by_title("  ")

def test_find_movies_by_title_type_check():
    svc = MovieService(MockMovieRepo())

    with pytest.raises(TypeError):
        svc.find_movies_by_title(123)

def test_get_movie_by_id_positive():
    svc = MovieService(MockMovieRepo())
    movie = svc.get_movie_by_id("mock_id")

    assert movie is not None
    assert str(movie.movie_id) == "mock_id"

def test_get_movie_by_id_type_check():
    svc = MovieService(MockMovieRepo())

    with pytest.raises(TypeError):
        svc.get_movie_by_id(123)

def test_remove_movie_positive():
    svc = MovieService(MockMovieRepo())
    svc.remove_movie("mock_id")

    assert svc.get_movie_by_id("mock_id") is None

def test_remove_movie_negative():
    svc = MovieService(MockMovieRepo())

    with pytest.raises(ValueError):
        svc.remove_movie("does_not_exist")

def test_update_movie_positive():
    svc = MovieService(MockMovieRepo())
    updated = make_movie(movie_id="mock_id", title="Updated Title")
    svc.update_movie(updated)
    movie = svc.get_movie_by_id("mock_id")

    assert movie is not None
    assert movie.title == "Updated Title"

def test_update_movie_negative():
    svc = MovieService(MockMovieRepo())
    updated = make_movie(movie_id="missing_id", title="Updated Title")

    with pytest.raises(ValueError):
        svc.update_movie(updated)