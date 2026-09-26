class Movie:
    def __init__(self, title, year, rating, overview, poster_path):
        self.title = title
        self.year = year
        self.rating = rating
        self.overview = overview
        self.poster_path = poster_path

    def __repr__(self) -> str:
        return f"Title: {self.title} | Rating: {self.rating} | Release Date: ({self.year}) | \n\n\n Description: {self.overview} \n\n\n Poster Path = https://image.tmdb.org/t/p/w500{self.poster_path}"
