import pandas as pd

df=pd.read_csv('tmdb-movies.csv')
sorted_df = df.sort_values(by='revenue', ascending=False)

# Access the top 10 movies by revenue
top_10_movies = sorted_df.head(10)
sorted_df = df.sort_values(by='revenue', ascending=True)
lowest_10_movies = sorted_df.head(10)
# sorted_df = df.sort_values(by='revenue', ascending=True)
# Display the top 10 movies
print("top 10 movies")
print(top_10_movies[['original_title', 'revenue']])
print("lowest 10 movies")
print(lowest_10_movies[['original_title', 'revenue']])
print(df.info())
# Group by release year and sum the revenue for each year
revenue_by_year = df.groupby('release_year')['revenue'].sum()

# Find the year with the highest total revenue
best_year = revenue_by_year.idxmax()
highest_revenue = revenue_by_year.max()

print(f"The best year by revenue is {best_year} with a total revenue of {highest_revenue:.2f}")

