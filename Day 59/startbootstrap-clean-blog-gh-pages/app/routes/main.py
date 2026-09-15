from flask import Blueprint, render_template
from app.utils import load_json

main_bp = Blueprint("main", __name__)

all_posts = load_json("all_posts.json")


@main_bp.route("/")
def main_page():
    data = load_json("all_posts.json")
    return render_template("index.html", data=data)
