from datetime import timedelta


class Config:
    SECRET_KEY = "your_secret_key_here"

    SQLALCHEMY_DATABASE_URI = "sqlite:///posts.db"

    DEBUG = True

    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    REMEMBER_COOKIE_DURATION = timedelta(days=30)
