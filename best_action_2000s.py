import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def best_action_movies(file_path='tmdb-movies.csv'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Filter movies released after the year 2000 and with the 'Action' genre
    df_after_2000_action = df[(df['release_year'] > 2000) & (df['genres'].str.contains('Action'))]

    # Sort the filtered DataFrame by revenue in descending order
    sorted_df = df_after_2000_action.sort_values(by='revenue', ascending=False)

    # Access the top 10 action movies by revenue
    top_10_action_movies = sorted_df.head(10)

    # Display the top 10 action movies
    print("Top 10 Action Movies After 2000:")
    print(top_10_action_movies[['original_title', 'revenue']])

    # Display DataFrame information
    print("\nDataFrame Info:")
    print(df.info())

    # Group by release year and sum the revenue for each year
    revenue_by_year = df.groupby('release_year')['revenue'].sum()

    # Find the year with the highest total revenue
    best_year = revenue_by_year.idxmax()
    highest_revenue = revenue_by_year.max()

    print(f"\nThe best year by revenue is {best_year} with a total revenue of {highest_revenue:.2f}")

    # Create a horizontal bar chart for the top 10 action movies using seaborn
    plt.figure(figsize=(12, 6))
    sns.barplot(x='revenue', y='original_title', data=top_10_action_movies.sort_values(by='revenue', ascending=False), palette='viridis')
    plt.xlabel('Revenue (in billions)')
    plt.ylabel('Movie Title')
    plt.title('Top 10 Action Movies After 2000 by Revenue')

    plt.tight_layout()
    plt.show()

# Call the function
best_action_movies()
