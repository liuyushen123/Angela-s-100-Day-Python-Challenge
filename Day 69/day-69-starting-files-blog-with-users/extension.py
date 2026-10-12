from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
bootstrap = Bootstrap5()
login_manager = LoginManager()
ckeditor = CKEditor()
login_manager.login_view = "auth.login"  # type: ignore
