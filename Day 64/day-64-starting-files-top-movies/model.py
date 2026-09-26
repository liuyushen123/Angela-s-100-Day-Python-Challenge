from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app, db


class MovieModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)

    @classmethod
    def get_all_movies(cls, sort_by="rating", descending=True):
        column = getattr(cls, sort_by, cls.rating)
        order = column.desc() if descending else column.asc()
        return db.session.execute(db.select(cls).order_by(order)).scalars().all()

    @classmethod
    def add_movie(cls, title, year, description, rating, review, img_url):

        movie = cls(
            title=title,  # type: ignore
            year=year,  # type: ignore
            description=description,  # type: ignore
            rating=rating,  # type: ignore
            review=review,  # type: ignore
            img_url=img_url,  # type: ignore
        )

        db.session.add(movie)
        db.session.commit()

    @classmethod
    def find_movie_by_id(cls, movie_id):
        return db.session.get(cls, movie_id)

    @classmethod
    def delete_movie(cls, movie_id):
        movie = cls.find_movie_by_id(movie_id)

        if movie:
            db.session.delete(movie)
            db.session.commit()

    def __repr__(self):
        return f"{self.title} ({self.year}) - {self.rating}/10"


if __name__ == "__main__":
    app = create_app()
