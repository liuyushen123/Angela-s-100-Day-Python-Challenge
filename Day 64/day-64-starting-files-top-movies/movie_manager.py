import requests
from movie_interface import Movie


class MovieManager:
    url = "https://api.themoviedb.org/3/search/movie"
    api_key = "f9eb624d725e60d1aec7676cf05ad029"
    headers = {"accept": "application/json"}

    @classmethod
    def find_movie(cls, title):
        params = {"api_key": cls.api_key, "query": title}
        matched_result = requests.get(
            url=cls.url, headers=cls.headers, params=params
        ).json()

        movies = []
        for movie in matched_result.get("results", []):
            title = movie.get("title")
            year = movie.get("release_date")
            rating = movie.get("vote_average")
            overview = movie.get("overview")
            poster_path = f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}"

            movies.append(Movie(title, year, rating, overview, poster_path))

        return movies
