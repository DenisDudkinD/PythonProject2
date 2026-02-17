from src.domain.review import Review
from src.repositories.review_repository_protocol import ReviewRepositoryProtocol


class MockReviewRepo(ReviewRepositoryProtocol):
    def get_all_reviews(self):
        return [
            Review(
                movie_id="mock_id",
                reviewer="Alice A",
                score=10,
                review_text="Very Good",
            )
        ]

    def add_review(self, review):
        return "mock_id"

    def get_review_by_id(self, review_id):
        return Review(
            movie_id="mock_id", reviewer="Alice A", score=10, review_text="Very Good"
        )

    def get_reviews_by_movie(self, movie_id):
        return [
            Review(
                movie_id="mock_id",
                reviewer="Alice A",
                score=10,
                review_text="Very Good",
            )
        ]

    def delete_review(self, review_id):
        pass

    def update_review(self, review):
        pass

    def add_seed_records(self, reviews):
        pass
