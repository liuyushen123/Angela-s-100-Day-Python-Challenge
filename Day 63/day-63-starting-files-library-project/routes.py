from flask import Flask, render_template, request, redirect, url_for, Blueprint
from form import BookForm, EditForm
from model import Book

routes_bp = Blueprint("route", __name__)


@routes_bp.route("/")
def home():
    all_books = Book.get_all()
    return render_template("index.html", books=all_books)


@routes_bp.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()

    if form.validate_on_submit():
        book_name = form.book_name.data
        author_name = form.author_name.data
        rating = form.rating.data

        Book.add(book_name, author_name, rating)
        return redirect(url_for("route.home"))

    return render_template("add.html", form=form)


@routes_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    book = Book.get_by_id(id)

    if form.validate_on_submit():
        Book.edit(id, rating=form.new_rating.data)
        return redirect(url_for("route.home"))

    return render_template("edit.html", book=book, form=form)


@routes_bp.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    Book.delete(id)

    return redirect(url_for("route.home"))
