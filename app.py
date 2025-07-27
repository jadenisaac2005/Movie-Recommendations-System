import pandas as pd
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

# --- Let's test our function! ---
# You can comment out or remove these lines when you build the Streamlit app
print("Backend logic is set up. Testing the recommendation function...")

movie_title = 'Dark Knight, The (2008)'
recommendations = get_recommendations(movie_title)
print(f"\nRecommendations for '{movie_title}':")
print(recommendations)

movie_title = 'Toy Story (1995)'
recommendations = get_recommendations(movie_title)
print(f"\nRecommendations for '{movie_title}':")
print(recommendations)
