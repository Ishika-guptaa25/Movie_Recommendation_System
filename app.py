import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API Key (replace with your own)
API_KEY = "ca6f504dfad07ddb9f6e0a31fd139481"

# Poster fetching function
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

API_KEY = "ca6f504dfad07ddb9f6e0a31fd139481"

# Create a session with retries
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()  # Raise error if status != 200
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/300x450.png?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print("⚠️ Error fetching poster:", e)
        return "https://via.placeholder.com/300x450.png?text=Poster+Error"



# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in distances:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# Streamlit UI
st.title("🎬 Movie Recommender with Posters")

selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])