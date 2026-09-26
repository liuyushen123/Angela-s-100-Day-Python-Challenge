from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from __init__ import create_app
from model import MovieModel
from form import MovieTitleForm
from movie_manager import MovieManager

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

app = create_app()


@app.route("/")
def home():
    sort_by = request.args.get("sort", "id")
    descending = request.args.get("order") == "desc"
    movies = MovieModel.get_all_movies(sort_by=sort_by, descending=descending)
    return render_template("index.html", movies=movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieTitleForm()
    if form.validate_on_submit():
        title = form.movie_title.data
        rating = form.movie_rating.data
        review = form.movie_review.data

        return redirect(url_for("select", title=title, rating=rating, review=review))

    return render_template("add.html", form=form)


@app.route("/select/<title>/<rating>/<review>", methods=["GET", "POST"])
def select(title, rating, review):
    movies = MovieManager.find_movie(title)
    return render_template("select.html", movies=movies, rating=rating, review=review)


@app.route("/add_movie", methods=["POST"])  # type: ignore
def add_movie():
    title = request.form.get("title")
    year = request.form.get("year")
    overview = request.form.get("overview")
    img_url = request.form.get("img_url")
    review = request.form.get("review")
    rating = request.form.get("rating")
    MovieModel.add_movie(
        title=title,
        year=year,
        description=overview,
        rating=rating,
        review=review,
        img_url=img_url,
    )

    return redirect(url_for("home"))


@app.route("/delete", methods=["POST"])
def delete():
    movie_id = request.form.get("movie_id")
    MovieModel.delete_movie(movie_id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=5001)
