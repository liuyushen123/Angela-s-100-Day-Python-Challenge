from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from extension import db, login_manager, bootstrap, ckeditor
from model.blog_post import BlogPost
from model.user import User


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    app.config.from_object("config.Config")

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    with app.app_context():
        db.create_all()

    from controller import blueprints

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
