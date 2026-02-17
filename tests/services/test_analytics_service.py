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
