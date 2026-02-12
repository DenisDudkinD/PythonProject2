from uuid import UUID
from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from src.repositories.actor_repository import SQLActorRepository
from src.repositories.cast_repository import SQLCastRepository
from src.repositories.movie_repository import MovieRepository
from src.repositories.review_repository import ReviewRepository
from src.repositories.studio_repository import StudioRepository
from src.services.actor_service import ActorService
from src.services.cast_service import CastService
from src.services.generator_service import generate
from src.services.movie_service import MovieService
from src.services.studio_service import StudioService
from src.services.review_service import ReviewService
from src.db.deps import get_db

app = FastAPI(title="Book API")

def get_actor_repository(db: Session = Depends(get_db)) -> SQLActorRepository:
    return SQLActorRepository(db)

def get_actor_service(repo: SQLActorRepository = Depends(get_actor_repository)) -> ActorService:
    return ActorService(repo)

def get_cast_repository(db: Session = Depends(get_db)) -> SQLCastRepository:
    return SQLCastRepository(db)

def get_cast_service(repo: SQLCastRepository = Depends(get_cast_repository)) -> CastService:
    return CastService(repo)

def get_movie_repository(db: Session = Depends(get_db)) -> MovieRepository:
    return MovieRepository(db)

def get_movie_service(repo: MovieRepository = Depends(get_movie_repository)) -> MovieService:
    return MovieService(repo)

def get_studio_repository(db: Session = Depends(get_db)) -> StudioRepository:
    return StudioRepository(db)

def get_studio_service(repo: StudioRepository = Depends(get_studio_repository)) -> StudioService:
    return StudioService(repo)

def get_review_repository(db: Session = Depends(get_db)) -> ReviewRepository:
    return ReviewRepository(db)

def get_review_service(repo: ReviewRepository = Depends(get_review_repository)) -> ReviewService:
    return ReviewService(repo)


@app.post("/generate")
def generate_seed_books(
    actor_svc: ActorService = Depends(get_actor_service),
    cast_svc: CastService = Depends(get_cast_service),
    studio_svc: StudioService = Depends(get_studio_service),
    movie_svc: MovieService = Depends(get_movie_service),
    review_svc: ReviewService = Depends(get_review_service),
):
    movies, studios, actors, casts, reviews = generate()
    studio_svc.add_seed_records(studios)
    movie_svc.add_seed_records(movies)
    actor_svc.add_seed_records(actors)
    cast_svc.add_seed_records(casts)
    review_svc.add_seed_records(reviews)
    return "Books were added to DB......"