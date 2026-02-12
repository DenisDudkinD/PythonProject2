from typing import Protocol
from src.domain.review import Review


class ReviewRepositoryProtocol(Protocol):
    def add_review(self, review: Review) -> None:
        ...

    def get_all_reviews(self) -> list[Review]:
        ...

    def get_reviews_by_movie(self, movie_id: str) -> list[Review]:
        ...
    
    def update_review(self, review: Review) -> None:
        ...

    def delete_review(self, review: Review) -> None:
        ...
    
    def add_seed_records(self, reviews: list[Review]) -> None:
        ...
