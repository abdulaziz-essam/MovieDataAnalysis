import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def best_action_movies(file_path='tmdb-movies.csv'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Prompt the user to input a release year
    user_input_year = int(input("Enter a release year: "))

    # Filter movies released after the user-specified year and with the 'Action' genre
    df_after_user_year_movies = df[(df['release_year'] == user_input_year)]

    # Sort the filtered DataFrame by revenue in descending order
    sorted_df = df_after_user_year_movies.sort_values(by='revenue', ascending=False)

    # Access the top 10 action movies by revenue
    top_10_action_movies = sorted_df.head(10)

    # Display the top 10 action movies
    print(f"Top 10 Movies After {user_input_year}:")
    print(top_10_action_movies[['original_title', 'revenue']])

    # Display DataFrame information
    print("\nDataFrame Info:")
    print(df.info())

    # Group by release year and sum the revenue for each year
    revenue_by_year = df.groupby('release_year')['revenue'].sum()

    # Find the year with the highest total revenue
    best_year = revenue_by_year.idxmax()
    highest_revenue = revenue_by_year.max()

    print(f"\nThe best year by revenue is {best_year} with a total revenue of {highest_revenue:.2f} million")

    # Convert the revenue values to millions for plotting using .loc
    top_10_action_movies.loc[:, 'revenue'] = top_10_action_movies['revenue'] / 1e6  # Convert to millions

    # Create a horizontal bar chart for the top 10 action movies using seaborn
    plt.figure(figsize=(12, 6))
    sns.barplot(x='revenue', y='original_title', data=top_10_action_movies.sort_values(by='revenue', ascending=False), hue='original_title', palette='viridis', legend=False)
    plt.xlabel('Revenue (in millions)')
    plt.ylabel('Movie Title')
    plt.title(f'Top 10 Action Movies After {user_input_year} by Revenue')

    plt.tight_layout()
    plt.show()

# Call the function
best_action_movies()

