from flask import Flask


def create_app():
    app = Flask(__name__)

    from routes.authentication import authentication_bp
    from routes.home import home_bp
    from routes.check import check_bp

    app.register_blueprint(authentication_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(check_bp, url_prefix="/check")
    app.config.from_object("config.Config")

    return app
