from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from app.routes.main import main_bp
    from app.routes.blog import blog_bp
    from app.routes.pages import pages_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(pages_bp)

    return app
