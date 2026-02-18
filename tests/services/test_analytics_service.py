import pytest
import uuid

from src.services.movie_analytics_service import MovieAnalyticsService
from src.domain.movie import Movie
from src.domain.studio import Studio
from src.domain.review import Review
from src.domain.actor import Actor
from src.domain.cast import Cast


def test_average_review_score_positive():
    svc: MovieAnalyticsService = MovieAnalyticsService()
    reviews: list[Review] = []
    reviews.append(
        Review(movie_id=uuid.uuid4(), reviewer_name="", score=9, review_text="")
    )
    reviews.append(
        Review(movie_id=uuid.uuid4(), reviewer_name="", score=8, review_text="")
    )

    average_score = svc.average_review_score(reviews)

    assert average_score == 8.5


def test_average_revenue_positive():
    svc: MovieAnalyticsService = MovieAnalyticsService()
    movies: list[Movie] = []
    movies.append(Movie(studio_id=uuid.uuid4(), title="", revenue=2000))
    movies.append(Movie(studio_id=uuid.uuid4(), title="", revenue=1000))

    average_revenue = svc.average_revenue(movies)

    assert average_revenue == 1500


def test_average_revenue_by_rating_positive():
    svc: MovieAnalyticsService = MovieAnalyticsService()
    movies: list[Movie] = []
    movies.append(Movie(studio_id=uuid.uuid4(), title="", revenue=2000, rating="PG"))
    movies.append(Movie(studio_id=uuid.uuid4(), title="", revenue=1000, rating="PG"))
    movies.append(Movie(studio_id=uuid.uuid4(), title="", revenue=4000, rating="R"))
    movies.append(Movie(studio_id=uuid.uuid4(), title="", revenue=3000, rating="R"))

    revenue_by_rating = svc.average_revenue_by_rating(movies)

    assert revenue_by_rating["PG"] == 1500
    assert revenue_by_rating["R"] == 3500


def test_cast_size_by_movie_positive():
    svc: MovieAnalyticsService = MovieAnalyticsService()
    movies: list[Movie] = []
    movies.append(Movie(studio_id=uuid.uuid4(), title="A", revenue=2000, rating="PG"))
    casts: list[Cast] = []
    casts.append(
        Cast(
            movie_id=movies[0].movie_id,
            actor_id=uuid.uuid4(),
            role_type="",
            character_name="",
            billing_order=10,
        )
    )

    cast_sizes = svc.cast_size_by_movie(movies, casts)

    assert cast_sizes["A"] == 1


def test_actors_by_number_of_roles_positive():
    svc: MovieAnalyticsService = MovieAnalyticsService()
    actors: list[Actor] = []
    actors.append(Actor(full_name="A", nationality="USA"))
    casts: list[Cast] = []
    casts.append(
        Cast(
            movie_id=uuid.uuid4(),
            actor_id=actors[0].actor_id,
            role_type="",
            character_name="",
            billing_order=10,
        )
    )

    actor_roles = svc.actors_by_number_of_roles(actors, casts)

    assert actor_roles["A"] == 1


def test_studios_by_average_review_score_positive():
    svc: MovieAnalyticsService = MovieAnalyticsService()
    studios: list[Studio] = []
    studios.append(Studio(name="A", country="USA"))
    movies: list[Movie] = []
    movies.append(Movie(studio_id=studios[0].studio_id, title=""))
    movies.append(Movie(studio_id=studios[0].studio_id, title=""))
    reviews: list[Review] = []
    reviews.append(
        Review(movie_id=movies[0].movie_id, reviewer_name="", score=8, review_text="")
    )
    reviews.append(
        Review(movie_id=movies[0].movie_id, reviewer_name="", score=7, review_text="")
    )
    reviews.append(
        Review(movie_id=movies[1].movie_id, reviewer_name="", score=5, review_text="")
    )

    studio_scores = svc.studios_by_average_review_score(studios, movies, reviews)

    assert studio_scores["A"] == 20 / 3
