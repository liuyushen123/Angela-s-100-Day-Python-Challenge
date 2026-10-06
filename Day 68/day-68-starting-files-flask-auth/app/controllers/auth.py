from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from app.extensions import db
from app.models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]

        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            flash("That email is already registered. Log in instead.")
            return redirect(url_for("auth.login"))

        user = User(email=email, name=request.form["name"])  # type: ignore
        user.set_password(request.form["password"])
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for("main.secrets"))
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.session.execute(
            db.select(User).where(User.email == request.form["email"])
        ).scalar()
        if user and user.check_password(request.form["password"]):
            login_user(user)
            return redirect(url_for("main.secrets"))
        flash("Invalid email or password.")
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
