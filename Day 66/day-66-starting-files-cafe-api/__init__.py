from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.json.sort_keys = False  # type: ignore
    bootstrap.init_app(app)
    db.init_app(app)

    from controller import routes_bp

    app.register_blueprint(routes_bp)

    return app
