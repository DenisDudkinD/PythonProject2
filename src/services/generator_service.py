import random
import uuid
from datetime import date, datetime, timedelta
import numpy as np

from src.domain.movie import Movie
from src.domain.studio import Studio
from src.domain.actor import Actor
from src.domain.cast import Cast
from src.domain.review import Review

def generate(movie_count=100, studio_count=10, actor_count=100, cast_count=200, seed=None):
    rng = np.random.default_rng(seed)
    random.seed(seed)

    countries = [
        "USA",
        "Canada",
        "Mexico",
        "China",
        "Japan",
        "India",
        "UK",
        "France",
        "Spain",
        "Germany",
        "Italy"
    ] # can change or add more later

    ratings = [
        "G",
        "PG",
        "PG-13",
        "R",
        "NC-17",
        "NR"
    ]

    movies = []
    studios = []
    actors = []
    casts = []
    reviews = []

    for i in range(studio_count):
        studio_id = str(uuid.uuid4())
        studio = Studio(
            studio_id = studio_id,
            name = f"Studio{i}",
            country = rng.choice(countries),
            founded_year = int(rng.integers(1925, 2025))
        )
        studios.append(studio)

    for i in range(actor_count):
        actor_id = str(uuid.uuid4())
        actor = Actor(
            actor_id = actor_id,
            full_name = f"First{i} Last{i}",
            birth_date = datetime.now() - timedelta(days = int(rng.integers(7000,30000))),
            nationality = rng.choice(countries)
        )
        actors.append(actor)

    for i in range(movie_count):

        studio = studios[i%studio_count]
        studio_id = studio.studio_id

        movie_id = str(uuid.uuid4())
        review_id = str(uuid.uuid4())
        review_score = int(rng.integers(1,10))
        review_text = ["Very Bad", "Bad", "Good", "Very Good"][review_score//3]

        movie = Movie(
            movie_id = movie_id,
            studio_id = studio_id,
            title = f"Movie {i}",
            release_date = date.today() - timedelta(days = int(rng.integers(1, 3600))),
            runtime_minutes = int(rng.integers(80, 180)),
            rating = rng.choice(ratings),
            sequel_to_movie_id = movies[-1].movie_id if (movies and random.random() < 0.2) else None
        )

        review = Review(
            review_id = review_id,
            movie_id = movie_id,
            reviewer_name = f"Reviewer{i}",
            score = review_score,
            review_text = review_text
        )

        movies.append(movie)
        reviews.append(review)

    for i in range(cast_count):
        movie_id = rng.choice(movies).movie_id
        actor_id = rng.choice(actors).actor_id
        cast = Cast(
            movie_id = movie_id,
            actor_id = actor_id,
            role_type = rng.choice(["Leading", "Supporting"]),
            character_name = f"Character{i}",
            billing_order = int(rng.integers(10, 50))
        )
        casts.append(cast)

    return movies, studios, actors, casts, reviews
