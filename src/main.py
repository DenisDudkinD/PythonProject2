from uuid import UUID
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.repositories.actor_repository import SQLActorRepository
from src.repositories.cast_repository import SQLCastRepository
from src.repositories.movie_repository import MovieRepository
from src.repositories.review_repository import ReviewRepository
from src.repositories.studio_repository import StudioRepository
from src.domain.actor import Actor
from src.domain.cast import Cast
from src.domain.studio import Studio
from src.domain.review import Review
from src.dto.actor import ActorRead, ActorCreate
from src.dto.cast import CastRead, CastCreate
from src.dto.movie import MovieCreate, MovieRead, MovieUpdate
from src.dto.review import ReviewCreate, ReviewRead
from src.domain.movie import Movie
from src.dto.studio import StudioRead, StudioCreate
from src.services.actor_service import ActorService
from src.services.cast_service import CastService
from src.services.generator_service import generate
from src.services.movie_service import MovieService
from src.services.studio_service import StudioService
from src.services.review_service import ReviewService
from src.services.movie_analytics_service import MovieAnalyticsService
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

def get_movie_analytics_service() -> MovieAnalyticsService:
    return MovieAnalyticsService()

@app.exception_handler(HTTPException)
async def http_exception_handler(request:Request,exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail":exc.detail}
    )

@app.exception_handler(Exception)
async def global_exception_handler(request:Request, exc: Exception):
    return JSONResponse(
        status_code = 500,
        content={"detail":"Internal Server Error"}
    )


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
    return "Records were added to DB......"

#Actors endpoints
@app.get("/actors", response_model=list[ActorRead])
def list_actors(svc: ActorService = Depends(get_actor_service)):
    return svc.get_all_actors()

@app.put("/actors/{actor_id}", response_model=ActorRead)
def get_actor(actor_id:str, payload: ActorCreate, svc: ActorService = Depends(get_actor_service)):
    actor = Actor(**payload.model_dump())
    actor.actor_id = actor_id # type: ignore
    svc.update_actor(actor)
    return actor

@app.post("/actors", response_model=str)
def create_actor(payload: ActorCreate, 
                svc: ActorService = Depends(get_actor_service)
    ):
    actor = Actor(**payload.model_dump())
    actor_id = svc.add_actor(actor)
    return actor_id

@app.delete("/actors/{actor_id}", response_model=str)
def delete_actor( 
    actor_id: str,
    svc:ActorService = Depends(get_actor_service)
    ):
    try:
        svc.remove_actor_by_id(actor_id)
        return f"Actor {actor_id} deleted"
    except IntegrityError as e:
        raise HTTPException(status_code=400,detail="Can not delete, actor is foreign key in another table.") from e
    



#Casts endpoints
@app.get("/casts", response_model=list[CastRead])
def list_casts(svc: CastService = Depends(get_cast_service)):
    return svc.get_all_casts()

@app.post("/casts", response_model=str)
def create_cast(payload: CastCreate, 
                svc: CastService = Depends(get_cast_service)
    ):
    cast = Cast(**payload.model_dump())
    svc.add_cast(cast)
    return "cast_created"

@app.delete("/casts", response_model=str)
def delete_cast( 
    movie_id: str = Query(...),
    actor_id: str = Query(...),
    svc:CastService = Depends(get_cast_service)
    ):
    svc.remove_cast(movie_id,actor_id)
    return f"cast {movie_id} and {actor_id} deleted"


# Studios endpoints
@app.get("/studios", response_model=list[StudioRead])
def list_studios(svc: StudioService = Depends(get_studio_service)):
    return svc.get_all_studios()

@app.post("/studios", response_model=str)
def add_studio(payload: StudioCreate, svc: StudioService = Depends(get_studio_service)):
    studio = Studio(**payload.model_dump())
    studio_id = svc.add_studio(studio)
    return studio_id

@app.delete("/studios", response_model=str)
def delete_studio(
    studio_id: str = Query(...),
    svc: StudioService = Depends(get_studio_service)
    ):
    try: 
        svc.remove_studio_by_id(studio_id)
        return f"Studio deleted - id={studio_id}"
    except IntegrityError as e:
        raise HTTPException(status_code=400,detail="Can not delete, studio is foreign key in another table.") from e

@app.put("/studios/{studio_id}", response_model=StudioRead)
def update_studio(studio_id:str, payload: StudioCreate, svc: StudioService = Depends(get_studio_service)):
    studio = Studio(**payload.model_dump())
    studio.studio_id = studio_id # type: ignore
    svc.update_studio(studio_id, studio)
    return studio

# Movies endpoints
@app.post("/movies", response_model=str)
def create_movie(
    payload: MovieCreate,
    movie_svc: MovieService = Depends(get_movie_service),
):
    try:
        movie = Movie(**payload.model_dump())
        movie_id = movie_svc.add_movie(movie)
        return movie_id
    except IntegrityError as e:
        raise HTTPException(status_code=409, detail="Database constraint violation while creating movie") from e

@app.get("/movies", response_model=list[MovieRead])
def list_movies(movie_svc: MovieService = Depends(get_movie_service)):
    movies = movie_svc.get_all_movies()
    return movies

@app.get("/movies/search", response_model=list[MovieRead])
def search_movies(
    title: str = Query(..., min_length=1),
    movie_svc: MovieService = Depends(get_movie_service),
):
    movies =  movie_svc.find_movies_by_title(title)

    if not movies:
        raise HTTPException(status_code=404, detail="No movie found")

    return movies

@app.delete("/movies/{movie_id}")
def delete_movie(
    movie_id: str,
    movie_svc: MovieService = Depends(get_movie_service),
):
    try:
        movie_svc.remove_movie(movie_id)
        return f"Movie deleted - id={movie_id}"
    except ValueError as e:
        raise HTTPException(status_code=404, detail="Movie not found") from e

@app.patch("/movies/{movie_id}")
def update_movie(
    movie_id: str,
    payload: MovieUpdate,
    db: Session = Depends(get_db),
):
    movie = db.get(Movie, movie_id)

    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    data = payload.model_dump(exclude_unset=True)

    if not data:
        raise HTTPException(status_code=400, detail="No fields provide to update")

    for k, v in data.items():
        setattr(movie, k, v)

    db.commit()
    return f"Movie updated - id={movie_id}"

# Review endpoints
@app.post("/reviews", response_model=str)
def create_review(
    payload: ReviewCreate,
    review_svc: ReviewService = Depends(get_review_service)
):
    review = Review(**payload.model_dump())
    review_svc.add_review(review)
    return review.review_id

@app.get("/reviews", response_model=list[ReviewRead])
def all_reviews(review_svc: ReviewService = Depends(get_review_service)):
    reviews = review_svc.get_all_reviews()
    return reviews

@app.get("/movies/{movie_id}/reviews", response_model=list[ReviewRead])
def reviews_by_movie(
    movie_id: str,
    review_svc: ReviewService = Depends(get_review_service)
):
    reviews = review_svc.get_reviews_by_movie(movie_id)
    return reviews

@app.delete("/reviews/{review_id}")
def delete_review(
    review_id: str,
    review_svc: ReviewService = Depends(get_review_service)
):
    review_svc.delete_review(review_id)
    return f"Successfully deleted review with ID '{review_id}'"

@app.patch("/reviews/{review_id}", response_model=ReviewRead)
def update_review(
    review_id: str,
    payload: ActorCreate,
    review_svc: ReviewService = Depends(get_review_service)
):
    review = Review(**payload.model_dump())
    review.review_id = review_id # type: ignore
    review_svc.update_review(review)
    return review

# Analytics Endpoints
@app.get("/analytics/average_score")
def average_review_score(
    analytics: MovieAnalyticsService = Depends(get_movie_analytics_service),
    review_svc: ReviewService = Depends(get_review_service),
):
    reviews = review_svc.get_all_reviews()
    if not reviews:
        return {"average_score": None}
    return {"average_score": analytics.average_review_score(reviews)}

@app.get("/analytics/average_revenue")
def average_revenue(
    analytics: MovieAnalyticsService = Depends(get_movie_analytics_service),
    movie_svc: MovieService = Depends(get_movie_service),
):
    movies = movie_svc.get_all_movies()
    if not movies:
        return {"average_revenue": None}
    return {"average_revenue": analytics.average_revenue(movies)}

@app.get("/analytics/average_revenue_by_rating")
def average_revenue_by_rating(
    analytics: MovieAnalyticsService = Depends(get_movie_analytics_service),
    movie_svc: MovieService = Depends(get_movie_service),
):
    movies = movie_svc.get_all_movies()
    if not movies:
        return {"average_revenue_by_rating": None}
    return analytics.average_revenue_by_rating(movies)

@app.get("/analytics/cast_sizes")
def cast_sizes(
    analytics: MovieAnalyticsService = Depends(get_movie_analytics_service),
    movie_svc: MovieService = Depends(get_movie_service),
    cast_svc: CastService = Depends(get_cast_service),
):
    movies = movie_svc.get_all_movies()
    casts = cast_svc.get_all_casts()
    return analytics.cast_size_by_movie(movies, casts)

@app.get("/analytics/actors_by_number_of_roles")
def actors_by_number_of_roles(
    analytics: MovieAnalyticsService = Depends(get_movie_analytics_service),
    actor_svc: ActorService = Depends(get_actor_service),
    cast_svc: CastService = Depends(get_cast_service),
):
    actors = actor_svc.get_all_actors()
    casts = cast_svc.get_all_casts()
    return analytics.actors_by_number_of_roles(actors, casts)

@app.get("/analytics/studios_average_scores")
def studios_average_scores(
    analytics: MovieAnalyticsService = Depends(get_movie_analytics_service),
    studio_svc: StudioService = Depends(get_studio_service),
    movie_svc: MovieService = Depends(get_movie_service),
    review_svc: ReviewService = Depends(get_review_service),
):
    studios = studio_svc.get_all_studios()
    movies = movie_svc.get_all_movies()
    reviews = review_svc.get_all_reviews()
    return analytics.studios_by_average_review_score(studios, movies, reviews)
