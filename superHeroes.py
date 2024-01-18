import pandas as pd
import matplotlib.pyplot as plt

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

    # Create a bar chart for the best and worst Marvel and DC movies
    labels = ['Best Marvel', 'Worst Marvel', 'Best DC', 'Worst DC']
    revenues = [
        best_marvel_movie['revenue'],
        worst_marvel_movie['revenue'],
        best_dc_movie['revenue'],
        worst_dc_movie['revenue']
    ]

    movie_names = [
        best_marvel_movie['original_title'],
        worst_marvel_movie['original_title'],
        best_dc_movie['original_title'],
        worst_dc_movie['original_title']
    ]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, revenues, color=['green', 'red', 'blue', 'orange'])
    plt.title('Best and Worst Marvel/DC Movies by Revenue')
    plt.xlabel('Movie Type')
    plt.ylabel('Revenue (in billions)')

    # Display movie names on the x-axis
    plt.xticks(labels, movie_names, rotation=45, ha='right')

    plt.show()

# Call the function
analyze_movies()
