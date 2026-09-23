from sqlalchemy.orm import Mapped, mapped_column
from __init__ import db


class Book(db.Model):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    rating: Mapped[float]

    @classmethod
    def get_all(cls):
        return db.session.execute(db.select(cls)).scalars().all()

    @classmethod
    def create_table(cls):
        db.create_all()

    @classmethod
    def add(cls, title, author, rating):
        book = cls(
            title=title,  # type: ignore
            author=author,  # type: ignore
            rating=rating,  # type: ignore
        )

        db.session.add(book)
        db.session.commit()

    @classmethod
    def get_by_id(cls, book_id):
        return db.session.get(cls, book_id)

    @classmethod
    def edit(cls, book_id, rating=None):
        book = cls.get_by_id(book_id)

        if book:
            book.rating = rating  # type: ignore
            db.session.commit()

    @classmethod
    def delete(cls, book_id):
        book = cls.get_by_id(book_id)

        if book:
            db.session.delete(book)
            db.session.commit()
