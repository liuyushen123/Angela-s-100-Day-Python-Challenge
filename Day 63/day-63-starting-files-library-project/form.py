from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, URL, NumberRange


class BookForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    author_name = StringField("Book Author", validators=[DataRequired()])
    rating = IntegerField(
        "Rating", validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    submit = SubmitField("Submit")


class EditForm(FlaskForm):
    new_rating = IntegerField(
        "Rating", validators=[DataRequired(), NumberRange(min=1, max=10)]
    )
    submit = SubmitField("Submit")
