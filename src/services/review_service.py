from src.domain.review import Review
from src.repositories.review_repository_protocol import ReviewRepositoryProtocol


class ReviewService:
    def __init__(self, repo: ReviewRepositoryProtocol):
        self.repo: ReviewRepositoryProtocol = repo
    
    
