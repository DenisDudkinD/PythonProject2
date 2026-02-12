from src.domain.review import Review
from src.repositories.review_repository_protocol import ReviewRepositoryProtocol


class ReviewService:
    def __init__(self, repo: ReviewRepositoryProtocol):
        self.repo: ReviewRepositoryProtocol = repo
    
    def add_review(self, review: Review) -> None:
        if not isinstance(review, Review):
            raise TypeError("Expected Review, got something else.")
        self.repo.add_review(review)

    def get_all_reviews(self) -> list[Review]:
        return self.repo.get_all_reviews()

    def get_reviews_by_movie(self, movie_id: str) -> list[Review]:
        if not isinstance(movie_id, str):
            raise TypeError("Expected String, got something else.")
        if not movie_id.strip():
            raise ValueError("Query cannot be empty.")
        return self.repo.get_reviews_by_movie(movie_id)
    
    def update_review(self, review: Review) -> None:
        if not isinstance(review, Review):
            raise TypeError("Expected Review, got something else.")
        self.repo.update_review(review)

    def delete_review(self, review: Review) -> None:
        if not isinstance(review, Review):
            raise TypeError("Expected Review, got something else.")
        self.repo.delete_review(review)
    
    def add_seed_records(self, reviews: list[Review]) -> None:
        self.repo.add_seed_records(reviews)
