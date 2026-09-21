from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[
            DataRequired(),
            Email(granular_message=True, check_deliverability=False),
        ],
    )
    password = PasswordField(
        label="Password", validators=[DataRequired(), Length(min=6)]
    )
    submit = SubmitField(label="Login")
