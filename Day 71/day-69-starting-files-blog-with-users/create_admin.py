from __init__ import create_app
from extension import db
from model.user import User
import psycopg2


def create_admin(email: str, name: str, password: str) -> User:
    if User.user_exists(email):
        raise ValueError(f"{email} already exists")

    admin = User(email=email, name=name, is_admin=True)  # type: ignore
    admin.set_password(password)
    admin.add_user()
    return admin


if __name__ == "__main__":
    db_host = "database-1.c0b46qa44uxq.us-east-1.rds.amazonaws.com"
    db_name = "blog"  # replace with your actual database name
    db_user = "postgres"  # replace with your actual database user
    db_password = "liuyuchen00125"  # replace with your actual database password
    db_port = 5432  # replace with your actual database port if different
    conn = psycopg2.connect(
        host=db_host, dbname=db_name, user=db_user, password=db_password, port=db_port
    )
    app = create_app()
    with app.app_context():
        db.create_all()
        email = input("Email: ")
        password = input("Password: ")
        name = input("Name: ")

        try:
            admin = create_admin(email, name, password)
        except ValueError as e:
            print(e)
            raise ValueError("Cannot create admin")

        print(f"admin created：{admin.email}")
