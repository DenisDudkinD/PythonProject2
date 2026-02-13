import numpy as np
import pandas as pd

from src.domain.studio import Studio
from src.domain.movie import Movie
from src.domain.actor import Actor
from src.domain.cast import Cast
from src.domain.review import Review


class MovieAnalyticsService:

    def average_review_score(self, reviews: list[Review]):
        review_scores = np.array([r.score for r in reviews], dtype=float)
        return float(review_scores.mean())

    def average_revenue(self, movies: list[Movie]) -> float:
        revenues = np.array([m.revenue for m in movies], dtype=float)
        return float(revenues.mean())

    def average_revenue_by_rating(self, movies: list[Movie]) -> dict[str, float]:
        df = pd.DataFrame(
            [
                {
                    "rating": m.rating,
                    "revenue": m.revenue,
                }
                for m in movies
            ]
        )
        rating_revenues = (
            df.groupby("rating")["revenue"]
            .mean()
            .sort_values(ascending=False)
            .astype(float)
            .to_dict()
        )
        return rating_revenues

    def cast_size_by_movie(
        self, movies: list[Movie], casts: list[Cast]
    ) -> dict[str, int]:
        movies_id_to_title = dict([(m.movie_id, m.title) for m in movies])
        casts_df = pd.DataFrame(
            [
                {
                    "title": movies_id_to_title[c.movie_id],
                    "actor_id": c.actor_id,
                }
                for c in casts
            ]
        )
        cast_sizes = (
            casts_df.groupby("title")["actor_id"]
            .count()
            .sort_values(ascending=False)
            .astype(int)
            .to_dict()
        )
        return cast_sizes

    def actors_by_number_of_roles(
        self, actors: list[Actor], casts: list[Cast]
    ) -> dict[str, int]:
        actors_id_to_name = dict([(a.actor_id, a.full_name) for a in actors])
        casts_df = pd.DataFrame(
            [
                {
                    "movie_id": c.movie_id,
                    "name": actors_id_to_name[c.actor_id],
                }
                for c in casts
            ]
        )
        actor_casts = (
            casts_df.groupby("name")["movie_id"]
            .count()
            .sort_values(ascending=False)
            .astype(int)
            .to_dict()
        )
        return actor_casts

    def studios_by_average_review_score(
        self, studios: list[Studio], movies: list[Movie], reviews: list[Review]
    ) -> dict[str, float]:
        studios_id_to_name = dict([(s.studio_id, s.name) for s in studios])
        reviews_df = pd.DataFrame(
            [
                {
                    "movie_id": r.movie_id,
                    "score": r.score,
                }
                for r in reviews
            ]
        )
        movies_df = pd.DataFrame(
            [
                {
                    "movie_id": m.movie_id,
                    "studio_name": studios_id_to_name[m.studio_id],
                }
                for m in movies
            ]
        )
        studio_average_scores = (
            pd.merge(reviews_df, movies_df, on="movie_id")
            .groupby("studio_name")["score"]
            .mean()
            .astype(float)
            .to_dict()
        )
        return studio_average_scores
