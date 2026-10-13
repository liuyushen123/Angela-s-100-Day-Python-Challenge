from flask import Blueprint, render_template, redirect, url_for, abort
from model.blog_post import BlogPost
from flask import flash
from forms.make_post_form import MakePostForm
from flask_login import current_user, login_required
from functools import wraps
from forms.comment_form import CommentForm
from model.comment import MakeComment
from utils.decorators import (
    admin_only,
    authenticated_user,
    author_or_admin,
    author_only,
)

main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET"])
def get_all_posts():
    posts = BlogPost.get_first_three_posts()
    return render_template("index.html", all_posts=posts)


@main_bp.route("/older_posts", methods=["GET"])
def older_posts():
    posts = BlogPost.get_all_posts()
    return render_template("index.html", all_posts=posts)


@main_bp.route("/make-post", methods=["GET", "POST"])
@authenticated_user
def make_post():
    form = MakePostForm()
    if form.validate_on_submit():
        BlogPost.create_post(
            title=form.title.data,
            subtitle=form.subtitle.data,
            img_url=form.img_url.data,
            body=form.body.data,
            author_id=current_user.id,  # type: ignore
        )
        return redirect(url_for("main.get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=False)


@main_bp.route("/show-post/<int:post_id>", methods=["GET"])
def show_post(post_id):
    post = BlogPost.get_post_by_id(post_id)
    if post is None:
        return abort(404)
    form = CommentForm()
    return render_template("post.html", post=post, comment_form=form)


@main_bp.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@author_or_admin
def edit_post(post_id):
    post = BlogPost.get_post_by_id(post_id)
    form = MakePostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data  # type: ignore
        post.subtitle = form.subtitle.data  # type: ignore
        post.img_url = form.img_url.data  # type: ignore
        post.body = form.body.data  # type: ignore
        BlogPost.update_post(post)
        return redirect(url_for("main.show_post", post_id=post.id))  # type: ignore
    return render_template("make-post.html", form=form, is_edit=True)


@main_bp.route("/add-comment/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):
    post = BlogPost.get_post_by_id(post_id)
    if post is None:
        abort(404)

    form = CommentForm()
    if form.validate_on_submit():
        comment = MakeComment(
            body=form.body.data,  # type: ignore
            author_id=current_user.id,  # type: ignore
            post_id=post.id,  # type: ignore
        )
        comment.add_comment()
    else:
        flash("Comment can't be empty.")

    return redirect(url_for("main.show_post", post_id=post_id))


@main_bp.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@main_bp.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")
