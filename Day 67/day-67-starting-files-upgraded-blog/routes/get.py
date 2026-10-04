from flask import render_template, redirect, url_for, Blueprint
from model import BlogPost
from forms.make_post_form import MakePostForm
from datetime import date

get_bp = Blueprint("get", __name__)


@get_bp.route("/")
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = BlogPost.get_all_posts()
    return render_template("index.html", all_posts=posts)


@get_bp.route("/show-post/<int:post_id>")
def show_post(post_id):
    post = BlogPost.get_post_by_id(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return redirect(url_for("routes.get_all_posts"))


@get_bp.route("/update-post", methods=["GET", "POST"])
def update_post():
    form = MakePostForm()
    if form.validate_on_submit():
        BlogPost.add_post(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=date.today().strftime("%B %d, %Y"),
        )
        return redirect(url_for("get.get_all_posts"))
    return render_template("make-post.html", form=form)


@get_bp.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post_by_id(post_id):
    post = BlogPost.get_post_by_id(post_id)

    edit_form = MakePostForm(
        title=post.title,  # type: ignore
        subtitle=post.subtitle,  # type: ignore
        author=post.author,  # type: ignore
        img_url=post.img_url,  # type: ignore
        body=post.body,  # type: ignore
    )

    if edit_form.validate_on_submit():
        BlogPost.update_post(
            post_id=post_id,
            title=edit_form.title.data,
            subtitle=edit_form.subtitle.data,
            author=edit_form.author.data,
            img_url=edit_form.img_url.data,
            body=edit_form.body.data,
        )

        return redirect(url_for("get.get_all_posts"))

    return render_template("make-post.html", form=edit_form, is_edit=True)


@get_bp.route("/delete-post/<int:post_id>")
def delete_post_by_id(post_id):
    BlogPost.delete_post_by_id(post_id)
    return redirect(url_for("get.get_all_posts"))


@get_bp.route("/about")
def about():
    return render_template("about.html")


@get_bp.route("/contact")
def contact():
    return render_template("contact.html")
