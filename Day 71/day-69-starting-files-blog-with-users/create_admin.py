from __init__ import create_app
from extension import db
from model.user import User


def create_admin(email: str, name: str, password: str) -> User:
    if User.user_exists(email):
        raise ValueError(f"{email} already exists")

    admin = User(email=email, name=name, is_admin=True)  # type: ignore
    admin.set_password(password)
    admin.add_user()
    return admin


if __name__ == "__main__":
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
