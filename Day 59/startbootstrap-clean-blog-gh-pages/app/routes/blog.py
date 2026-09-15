from flask import Blueprint, render_template
from app.utils import load_json
from app.routes.main import all_posts

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/sample_post_page")
def sample_post_page():
    sample_post = load_json("sample.json")
    return render_template("post.html", post=sample_post)


@blog_bp.route("/post/<int:post_id>")
def post_page(post_id):
    post = next((p for p in all_posts if p["id"] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template("post.html", post=post)
