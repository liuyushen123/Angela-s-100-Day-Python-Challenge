from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):

    cafe = StringField("Cafe name", validators=[DataRequired()])

    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )

    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])

    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])

    coffee_rating = SelectField(
        "Coffee Rating",
        choices=[
            ("☕️", "☕️"),
            ("☕☕", "☕☕"),
            ("☕☕☕", "☕☕☕"),
            ("☕☕☕☕", "☕☕☕☕"),
            ("☕☕☕☕☕", "☕☕☕☕☕"),
        ],
        validators=[DataRequired()],
    )

    wifi_rating = SelectField(
        "Wifi Strength Rating",
        choices=[
            ("✘", "✘"),
            ("💪", "💪"),
            ("💪💪", "💪💪"),
            ("💪💪💪", "💪💪💪"),
            ("💪💪💪💪", "💪💪💪💪"),
            ("💪💪💪💪💪", "💪💪💪💪💪"),
        ],
        validators=[DataRequired()],
    )

    power_rating = SelectField(
        "Power Socket Availability",
        choices=[
            ("✘", "✘"),
            ("🔌", "🔌"),
            ("🔌🔌", "🔌🔌"),
            ("🔌🔌🔌", "🔌🔌🔌"),
            ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
            ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"),
        ],
        validators=[DataRequired()],
    )

    submit = SubmitField("Submit")
