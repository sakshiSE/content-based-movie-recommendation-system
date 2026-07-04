import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open("models/movies.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))

# Title
st.title("🎬 Movie Recommendation System")

# Recommend function
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# User enters movie name
movie_name = st.text_input("Enter movie name")

# Button
if st.button("Show Recommendations"):

    if movie_name in movies["title"].values:

        recommendations = recommend(movie_name)

        st.subheader("Recommended Movies")

        for movie in recommendations:
            st.write("👉", movie)

    else:
        st.write("Movie not found!")