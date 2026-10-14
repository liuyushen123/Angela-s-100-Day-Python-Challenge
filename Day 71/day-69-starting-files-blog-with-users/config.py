import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-me")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DB_URI",
        "sqlite:///posts.db",
    )

    DEBUG = os.environ.get("FLASK_DEBUG", "false").lower() == "true"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
