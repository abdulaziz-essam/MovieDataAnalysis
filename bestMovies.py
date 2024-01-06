# movie_analysis.py

import pandas as pd

def best_movies(file_path='tmdb-movies.csv'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Sort DataFrame by revenue in descending order
    sorted_df = df.sort_values(by='revenue', ascending=False)

    # Access the top 10 movies by revenue
    top_10_movies = sorted_df.head(10)

    # Sort DataFrame by revenue in ascending order
    sorted_df = df.sort_values(by='revenue', ascending=True)

    # Access the lowest 10 movies by revenue
    lowest_10_movies = sorted_df.head(10)

    # Display the top 10 movies
    print("Top 10 Movies:")
    print(top_10_movies[['original_title', 'revenue']])

    # Display the lowest 10 movies
    print("\nLowest 10 Movies:")
    print(lowest_10_movies[['original_title', 'revenue']])

    # Display DataFrame information
    print("\nDataFrame Info:")
    print(df.info())

    # Group by release year and sum the revenue for each year
    revenue_by_year = df.groupby('release_year')['revenue'].sum()

    # Find the year with the highest total revenue
    best_year = revenue_by_year.idxmax()
    highest_revenue = revenue_by_year.max()

    print(f"\nThe best year by revenue is {best_year} with a total revenue of {highest_revenue:.2f}")
