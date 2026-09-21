from flask import Flask, Blueprint, render_template, session

check_bp = Blueprint("check", __name__)


@check_bp.route("/denied")
def denied():
    return render_template("denied.html")


@check_bp.route("/success")
def success():
    if session.get("authenticated"):
        session["authenticated"] = False
        return render_template("success.html")

    return "<h1>Please enter username and password</h1>"
