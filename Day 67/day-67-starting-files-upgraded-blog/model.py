from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from __init__ import db


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    @classmethod
    def get_all_posts(cls):
        return db.session.execute(db.select(cls)).scalars().all()

    @classmethod
    def get_post_by_id(cls, post_id):
        return db.session.get(cls, post_id)

    @classmethod
    def add_post(cls, title, subtitle, author, img_url, body, date):
        new_post = cls(
            title=title,  # tpye: ignore # type: ignore
            subtitle=subtitle,  # tpye: ignore # type: ignore
            author=author,  # tpye: ignore # type: ignore
            img_url=img_url,  # tpye: ignore # type: ignore
            body=body,  # tpye: ignore # type: ignore
            date=date,  # tpye: ignore # type: ignore
        )
        db.session.add(new_post)
        db.session.commit()

    @classmethod
    def update_post(cls, post_id, title, subtitle, author, img_url, body):
        post = db.session.get(cls, post_id)
        if post:
            post.title = title  # type: ignore
            post.subtitle = subtitle  # type: ignore
            post.author = author  # type: ignore
            post.img_url = img_url  # type: ignore
            post.body = body  # type: ignore
            db.session.commit()

    @classmethod
    def delete_post_by_id(cls, post_id):
        post = db.session.get(cls, post_id)
        if post:
            db.session.delete(post)
            db.session.commit()


if __name__ == "__main__":
    from __init__ import create_app

    app = create_app()

    with app.app_context():
        db.create_all()
