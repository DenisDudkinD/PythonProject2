from sqlalchemy.orm import Session

from src.domain.review import Review
from src.repositories.review_repository_protocol import ReviewRepositoryProtocol


class ReviewRepository(ReviewRepositoryProtocol):
    def __init__(self, session: Session):
        self.session = session

    def add_review(self, review: Review) -> None:
        self.session.add(review)
        self.session.commit()

    def get_all_reviews(self) -> list[Review]:
        return self.session.query(Review).all()

    def get_reviews_by_movie(self, movie_id: str) -> list[Review]:
        return self.session.query(Review).filter(Review.movie_id == movie_id).all()
    
    def update_review(self, review: Review) -> None:
        self.session.merge(review)
        self.session.commit()

    def delete_review(self, review_id: str) -> None:
        review = self.session.get(Review, review_id)
        if review is None:
            raise ValueError(f"Review with id '{review_id}' not found.")
        self.session.delete(review)
        self.session.commit()
    
    def add_seed_records(self, reviews: list[Review]) -> None:
        for review in reviews:
            self.session.add(review)
        self.session.commit()
