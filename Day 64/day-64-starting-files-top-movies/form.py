from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf import FlaskForm


class MovieTitleForm(FlaskForm):
    movie_title = StringField(
        "Movie Title",
        validators=[DataRequired()],
        render_kw={"placeholder": "Search a Movie..."},
    )

    movie_rating = FloatField(
        "Movie Rating",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=10, message="Rating must be between 0 and 10"),
        ],
        render_kw={"placeholder": "What's the Rating? (e.g. 7.5)"},
    )

    movie_review = StringField(
        "Movie Review",
        validators=[DataRequired()],
        render_kw={"placeholder": "Write a Review"},
    )

    submit = SubmitField("Add Movie")
