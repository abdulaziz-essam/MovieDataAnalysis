# movie_analysis.py
# // get first ten directors by movies revenue
import pandas as pd
import matplotlib.pyplot as plt

def best_director(file_path='tmdb-movies.csv'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Sort DataFrame by revenue in descending order
    sorted_df = df.sort_values(by='revenue', ascending=False)

    sample = 10

    # Access the top movies by revenue
    top_director = sorted_df.head(sample)

    # Print information about the DataFrame
    print("DataFrame Information:")

    # Print the top movies and their directors
    print("\nTop Directors:")
    print(top_director[['director']])
    all_directors = top_director['director'].tolist()

    unique_directors = set(all_directors)

    # If the length is less than 10, get additional movies
    while len(unique_directors) < 10:
        additional_movies = sorted_df.iloc[sample:sample + 1]
        sample += 1

        # Check for unique directors in additional movies
        additional_directors = set(additional_movies['director'].tolist())
        unique_directors.update(additional_directors)

    # Print the unique directors
    print("\nUnique Directors:")
    for director in unique_directors:
        print(director)

    print("\nTotal number of unique directors:", len(unique_directors))

    # Create a bar chart for the top directors and their revenue
    plt.figure(figsize=(10, 6))
    plt.bar(top_director['director'], top_director['revenue'], color='blue')
    plt.title('Top Directors by Revenue')
    plt.xlabel('Director')
    plt.ylabel('Revenue (in billions)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Call the function
best_director()
