# Find similar movies


import re
import numpy as np

from difflib import SequenceMatcher
from functools import lru_cache

from src.model_utils import load_artifacts


@lru_cache(maxsize=1)
def get_data():
    return load_artifacts()


def normalize_title(title):
    return re.sub(r"[^a-z0-9]", "", title.lower())


def recommend_movies(movie_title, n=5):

    movies, similarity = get_data()

    # Normalize movie titles
    normalized_titles = movies["title"].apply(normalize_title)

    search_title = normalize_title(movie_title)

    # Find the selected movie
    matches = np.flatnonzero(normalized_titles.eq(search_title).to_numpy())

    # Handle movie not found
    if len(matches) == 0:

        suggestions = []

        for title in movies["title"].unique():

            normalized = normalize_title(title)

            score = SequenceMatcher(None, search_title, normalized).ratio()

            if score >= 0.75:
                suggestions.append((title, score))

        suggestions.sort(key=lambda x: x[1], reverse=True)

        suggested_titles = [title for title, score in suggestions[:5]]

        raise ValueError(
            f"Movie not found. Suggestions: {suggested_titles}"
            if suggested_titles
            else "No similar movie titles found."
        )

    # Get movie index
    movie_index = matches[0]

    # Get similarity scores
    distances = similarity[movie_index]

    if hasattr(distances, "toarray"):
        distances = distances.toarray().flatten()
    else:
        distances = np.asarray(distances).flatten()

    # Sort recommendations
    sorted_movies = np.argsort(distances)[::-1]

    # Exclude selected movie
    sorted_movies = [index for index in sorted_movies if index != movie_index][:n]

    # Return recommendations
    recommendations = []

    for index in sorted_movies:

        recommendations.append(
            {
                "id": movies.iloc[index]["id"],
                "title": movies.iloc[index]["title"],
                "similarity_score": round(float(distances[index]), 3),
            }
        )

    return recommendations
