from flask_login import UserMixin
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from app.extensions import db


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(1000))

    def set_password(self, raw_password: str) -> None:
        self.password = generate_password_hash(
            raw_password, method="pbkdf2:sha256", salt_length=8
        )

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password, raw_password)

    def __repr__(self) -> str:
        return f"Email: {self.email}, Name: {self.name}, Password: {self.password}"
