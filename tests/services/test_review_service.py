import pytest

from src.services.review_service import ReviewService
from src.domain.review import Review
from tests.mocks.mock_review_repository import MockReviewRepo


def test_add_review_negative():
    review = 3
    repo = MockReviewRepo()
    svc = ReviewService(repo)

    with pytest.raises(TypeError) as e:
        svc.add_review(review)  # type: ignore

    assert str(e.value) == "Expected Review, got something else."


def test_get_reviews_by_movie_negative():
    movie_id = 3
    repo = MockReviewRepo()
    svc = ReviewService(repo)

    with pytest.raises(TypeError) as e:
        svc.get_review_by_id(movie_id)  # type: ignore

    assert str(e.value) == "Expected String, got something else."


def test_get_review_by_id_negative():
    review_id = 3
    repo = MockReviewRepo()
    svc = ReviewService(repo)

    with pytest.raises(TypeError) as e:
        svc.get_review_by_id(review_id)  # type: ignore

    assert str(e.value) == "Expected String, got something else."


def test_update_review_negative():
    review = 3
    repo = MockReviewRepo()
    svc = ReviewService(repo)

    with pytest.raises(TypeError) as e:
        svc.update_review(review)  # type: ignore

    assert str(e.value) == "Expected Review, got something else."


def test_delete_review_negative():
    review = 3
    repo = MockReviewRepo()
    svc = ReviewService(repo)

    with pytest.raises(TypeError) as e:
        svc.delete_review(review)  # type: ignore

    assert str(e.value) == "Expected String, got something else."
