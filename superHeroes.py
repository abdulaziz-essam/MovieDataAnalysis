# movie_analysis.py

import pandas as pd

def analyze_movies(file_path='tmdb-movies.csv'):
    df = pd.read_csv(file_path)

    # Filter Marvel movies released in 2008 or later with non-zero revenue
    marvel_movies = df[(df['release_year'] >= 2008) & (df['production_companies'].str.contains('Marvel')) & (df['revenue'] > 0)]

    # Filter DC movies released in 2008 or later with non-zero revenue
    dc_movies = df[(df['release_year'] >= 2008) & (df['production_companies'].str.contains('DC', case=False)) & (df['revenue'] > 0)]

    # Find the best and worst Marvel movies
    best_marvel_movie = marvel_movies.loc[marvel_movies['revenue'].idxmax()]
    worst_marvel_movie = marvel_movies.loc[marvel_movies['revenue'].idxmin()]

    # Find the best and worst DC movies
    best_dc_movie = dc_movies.loc[dc_movies['revenue'].idxmax()]
    worst_dc_movie = dc_movies.loc[dc_movies['revenue'].idxmin()]

    # Display details of the best and worst Marvel movies
    print("Best Marvel Movie:")
    print(best_marvel_movie[['original_title', 'revenue', 'budget', 'vote_average', 'release_year']])

    print("\nWorst Marvel Movie:")
    print(worst_marvel_movie[['original_title', 'revenue', 'budget', 'vote_average', 'release_year']])

    # Display details of the best and worst DC movies
    print("\nBest DC Movie:")
    print(best_dc_movie[['original_title', 'revenue', 'budget', 'vote_average', 'release_year']])

    print("\nWorst DC Movie:")
    print(worst_dc_movie[['original_title', 'revenue', 'budget', 'vote_average', 'release_year']])
