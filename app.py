import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Step 1: Load Data ---
movies = pd.read_csv('data/movies.csv')

# --- Step 2: Build the Content-Based Model ---
tfidf = TfidfVectorizer(stop_words='english')
movies['genres'] = movies['genres'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# --- Step 3: Create the Recommendation Function ---
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    """
    This function takes a movie title and the cosine similarity matrix,
    and returns a list of the 5 most similar movies.
    """
    # Get the index of the movie that matches the title
    try:
        idx = indices[title]
    except KeyError:
        return ["Movie not found."]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar movies (excluding the movie itself)
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    return movies['title'].iloc[movie_indices].tolist()

# --- FRONTEND ---
st.title('🎬 Movie Recommendation System')
st.write("Find movies similar to your favorites based on their genres.")

# Create a list of all movie titles for the dropdown menu
movie_list = movies['title'].unique()

# Create a select box with a placeholder and no default selection
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,
    index=None,  # This makes the default selection empty
    placeholder="Select a movie..."
)

# Create a button to trigger the recommendation
if st.button('Recommend'):
    # Add a check to ensure a movie was selected
    if selected_movie:
        with st.spinner('Finding recommendations...'):
            recommendations = get_recommendations(selected_movie)
            st.subheader(f"Because you liked {selected_movie}, you might also like:")
            for movie_title in recommendations:
                st.success(movie_title)
    else:
        st.warning("Please select a movie first.")
