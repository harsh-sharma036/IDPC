from src.MovieDataHandler import MovieDataHandler
from src.recommendation import Recommendation

if __name__ == "__main__":
    # Load and preprocess data
    print("Loading data...")
    data_handler = MovieDataHandler()
    train_data, test_data = data_handler.preprocess_data()

    # Initialize the recommender system
    recommender = Recommendation(train_data, data_handler.movies_frame)

    # Ask user for a movie ID
    try:
        print("\nWelcome to the Movie Recommendation System!")
        movie_id = int(input("Enter a Movie ID to get recommendations (e.g., 1): "))
        top_n = int(input("How many recommendations would you like? (e.g., 5): "))

        # Generate and display recommendations
        recommendations = recommender.recommend_similar_movies(movie_id, top_n)
        print(f"\nTop {top_n} movies similar to Movie ID {movie_id}:\n", recommendations)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
