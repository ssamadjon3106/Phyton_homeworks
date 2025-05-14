import requests
import random

# TMDB API Bearer Token (Keep it secure in real use)
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMDU3YWEwNTk1YjcwYTZmOWI2ZTk2N2Q5OGUxMmVkNiIsIm5iZiI6MTc0Njk2MTY1OC41OTMsInN1YiI6IjY4MjA4NGZhNTBiYjhmZTBiMDg2M2M5NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tDq7xgLda0ENSRR6ThTHOWmWLSzuLLnvyUw72Zc89aU"
}


genres_url = "https://api.themoviedb.org/3/genre/movie/list"
response = requests.get(genres_url, headers=headers)
genres = response.json().get("genres", {})

# Create mapping of genre name to ID
genre_dict = {genre["name"].lower(): genre["id"] for genre in genres}

# Step 2: Ask user for genre input
user_input = input("Enter a movie genre (e.g. Action, Comedy, Horror): ").lower()

if user_input not in genre_dict:
    print("Genre not found. Please try one from this list:")
    print(", ".join(genre_dict.keys()))
else:
    genre_id = genre_dict[user_input]

    # Step 3: Get movies by genre
    discover_url = f"https://api.themoviedb.org/3/discover/movie?with_genres={genre_id}&sort_by=popularity.desc"
    movie_response = requests.get(discover_url, headers=headers)
    movies = movie_response.json().get("results", [])

    if not movies:
        print("No movies found for that genre.")
    else:
        movie = random.choice(movies)
        print("\n🎬 Recommended Movie:")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Rating: {movie['vote_average']}")
        print(f"Release Date: {movie['release_date']}")
