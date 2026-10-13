# TODO: Create a User table for all your registered users.
from sqlalchemy import Integer, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from extension import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(1000), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("MakeComment", back_populates="author")

    def __repr__(self) -> str:
        return f"Email: {self.email}, \n Name: {self.name}"

    def add_user(self) -> None:
        db.session.add(self)
        db.session.commit()

    def set_password(self, raw_password: str) -> None:
        self.password = generate_password_hash(
            raw_password, method="pbkdf2:sha256", salt_length=8
        )

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password, raw_password)

    def get_avatar_url(self) -> str:
        return f"https://www.gravatar.com/avatar/{self.email.lower().encode('utf-8').hex()}?d=identicon"

    @classmethod
    def get_user_by_email(cls, email: str):
        return db.session.execute(db.select(cls).where(cls.email == email)).scalar()

    @classmethod
    def user_exists(cls, email: str) -> bool:
        user = cls.get_user_by_email(email)
        return user is not None


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
