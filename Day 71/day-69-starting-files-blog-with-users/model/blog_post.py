from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from __init__ import db
import datetime


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    author_id: Mapped[int] = mapped_column(
        Integer, db.ForeignKey("users.id"), nullable=False
    )
    author = relationship("User", back_populates="posts")  # type: ignore
    comments = relationship("MakeComment", back_populates="post")

    @classmethod
    def get_all_posts(cls):
        return db.session.execute(db.select(cls)).scalars().all()

    @classmethod
    def get_first_three_posts(cls):
        return db.session.execute(db.select(cls).limit(3)).scalars().all()

    @classmethod
    def create_post(cls, title, subtitle, img_url, body, author_id):
        post = cls(
            title=title,  # type: ignore
            subtitle=subtitle,  # type: ignore
            img_url=img_url,  # type: ignore
            body=body,  # type: ignore
            date=datetime.datetime.now().strftime("%B %d, %Y"),  # type: ignore
            author_id=author_id,  # type: ignore
        )
        db.session.add(post)
        db.session.commit()

    @classmethod
    def get_post_by_id(cls, post_id):
        return db.session.get(cls, post_id)

    @classmethod
    def update_post(cls, post):
        db.session.add(post)
        db.session.commit()
