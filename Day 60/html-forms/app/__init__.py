from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.pages import pages_bp

    app.register_blueprint(pages_bp)
    app.config.from_object("config.Config")

    return app
