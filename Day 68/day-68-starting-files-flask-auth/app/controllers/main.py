from flask import Blueprint, render_template, current_app, send_from_directory
from flask_login import login_required, current_user

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@main_bp.route("/download")
@login_required
def download():
    return send_from_directory(
        current_app.static_folder, "files/cheat_sheet.pdf", as_attachment=True  # type: ignore
    )
