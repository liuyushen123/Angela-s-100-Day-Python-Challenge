from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, current_user
from forms.register_form import RegisterForm
from forms.login_form import LoginForm
from model.user import User
from werkzeug.security import generate_password_hash

auth_bp = Blueprint("auth", __name__)


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data

        if email is not None and User.user_exists(email):
            flash("That email is already registered. Log in instead.")
            return redirect(url_for("auth.login"))
        new_user = User(email=email, name=name, is_admin=False)  # type: ignore
        new_user.set_password(form.password.data)  # type: ignore
        new_user.add_user()  # type: ignore
        login_user(new_user)  # type: ignore
        return redirect(url_for("main.get_all_posts"))
    return render_template("register.html", form=form)


# TODO: Retrieve a user from the database based on their email.
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email is not None:
            user = User.get_user_by_email(email)
            if user and user.check_password(password):
                login_user(user, remember=False)
                return redirect(url_for("main.get_all_posts"))
        flash("Invalid email or password.")
    return render_template("login.html", form=form, current_user=current_user)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.get_all_posts"))
