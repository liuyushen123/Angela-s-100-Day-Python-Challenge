from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from __init__ import db
import datetime


class MakeComment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow, nullable=False
    )
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))

    author = relationship("User", back_populates="comments")
    post = relationship("BlogPost", back_populates="comments")

    def __repr__(self) -> str:
        return f"Comment by {self.author.name} on {self.date}: {self.body}"

    def add_comment(self) -> None:
        db.session.add(self)
        db.session.commit()

    def display_date(self) -> str:
        return self.date.strftime("%B %d, %Y at %H:%M")

    @classmethod
    def get_comments_by_post_id(cls, post_id: int):
        return (
            db.session.execute(db.select(cls).where(cls.post_id == post_id))
            .scalars()
            .all()
        )

    @classmethod
    def get_comments_by_author_id(cls, author_id: int):
        return (
            db.session.execute(db.select(cls).where(cls.author_id == author_id))
            .scalars()
            .all()
        )

    @classmethod
    def get_comment_by_id(cls, comment_id: int):
        return db.session.execute(db.select(cls).where(cls.id == comment_id)).scalar()

    @classmethod
    def delete_comment_by_id(cls, comment_id: int) -> None:
        comment = cls.get_comment_by_id(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
