# streamlit frontend


import streamlit as st

from src.recommendation import recommend_movies

# Page configuration
st.set_page_config(
    page_title="Movie Recommendation System", page_icon="🎬", layout="wide"
)


# Application heading
st.title(" Movie Recommendation System")


# Movie search
movie_name = st.text_input(
    "Enter a movie name", placeholder="Example: Avatar, Spider-Man, Batman..."
)


# Recommendation button
if st.button("Get Recommendations"):

    if not movie_name.strip():

        st.warning("Please enter a movie name.")

    else:

        try:

            recommendations = recommend_movies(movie_name)

            st.subheader("Recommended Movies")

            for movie in recommendations:

                st.write(
                    f" **{movie['title']}** "
                    # f"| Similarity: {movie['similarity_score']}"
                )

        except ValueError as error:

            st.error(str(error))
