from flask import Flask, render_template, request, Blueprint, redirect, url_for, session
from form import LoginForm

authentication_bp = Blueprint("authentication", __name__)


@authentication_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data != "admin@example.com":
            print("User inputed incorrect email")

            return redirect(url_for("check.denied"))

        if form.password.data != "iLovePython126":
            print("User inputed incorrect password")

            return redirect(url_for("check.denied"))

        session["authenticated"] = True

        return redirect(url_for("check.success"))
    else:
        print(form.errors)

        return render_template("login.html", form=form)
