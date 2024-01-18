import pandas as pd
import matplotlib.pyplot as plt

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

    # Create a horizontal bar chart for the top 10 movies with custom colors (reversed order)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.barh(top_10_movies['original_title'], top_10_movies['revenue'], color=['#FF5733', '#FF8C00', '#FFD700', '#9ACD32', '#32CD32', '#00CED1', '#1E90FF', '#8A2BE2', '#FF69B4', '#FF1493'][::-1])
    plt.xlabel('Revenue (in billions)')
    plt.title('Top 10 Movies by Revenue (Reversed Order)')

    # Create a horizontal bar chart for the lowest 10 movies with custom colors and reversed order
    plt.subplot(1, 2, 2)
    plt.barh(lowest_10_movies['original_title'], lowest_10_movies['revenue'], color=['#FF5733', '#FF8C00', '#FFD700', '#9ACD32', '#32CD32', '#00CED1', '#1E90FF', '#8A2BE2', '#FF69B4', '#FF1493'][::-1])
    plt.xlabel('Revenue (in billions)')
    plt.title('Lowest 10 Movies by Revenue')

    plt.tight_layout()
    plt.show()

# Call the function
best_movies()
